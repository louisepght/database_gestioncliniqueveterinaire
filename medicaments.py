#!/usr/bin/python3
import psycopg2


def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'

def inserer_medicament(conn): #dans la perspective d'une prescription a un patient
	cur = conn.cursor()
	nom_molecule = quote(input("Entrez le nom de la molécule"))
	effets = quote(input("Décrivez les effets du médicament"))
	try :
		sql = "INSERT INTO Medicament VALUES (%s, %s);" %(nom_molecule, effets)
		cur.execute(sql)
		res = cur.fetchone()
		print("Le medicament (%s, %s) a été ajouté à votre base de données \n"%(res[0], res[1]))
		
		print("Un médicament est compatible avec au moins une espèce, combien d'espèces sont compatibles avec %s ?"%(nom_molecule))

		nb = int(input("Entrez un nombre entre 1 et 12 :"))
		while ((nb>12) or (nb<1)) :
			print("Votre nombre est incorrect, veuillez réessayer\n")
			nb = int(input("Entrez un nombre entre 1 et 12 :"))

		for i in range (1,nb) :
			categorie = quote(input("Entrez la catégorie de l'espèce : félin, canidé, oiseau, rongeur, reptile ou autre"))
			taille = quote(input("Entrez la taille de l'espèce : petite ou moyenne"))
			sql = "INSERT INTO Est_autorise VALUES (%s, %s, %s);" %(nom_molecule, categorie, taille)
			cur.execute(sql)
			res = cur.fetchall()
			for espece in res :
				print("L'espèce suivante est autorisée à recevoir le médicament %s : %s, %s\n"%(espece[0],espece[1],espece[2]))	
	
		conn.commit()

	except psycopg2.IntegrityError as e:
		conn.rollback()
		print("Message système :", e)

def modifier_medicament(conn):
	cur = conn.cursor()
	nom_molecule= quote(input("Quel médicament voulez-vous modifier ? Entrez le nom de sa molécule :"))

	decision = int(input("Tapez 1 pour mettre à jour le nom, 2 pour mettre à jour les effets, 3 pour le nom et les effets :"))

	while ((decision < 1) and (decision > 3)) :
		print("Le nombre entré ne renvoie à aucune option, veuillez réessayer\n")
		decision = int(input("Tapez 1 pour mettre à jour le nom, 2 pour mettre à jour les effets, 3 pour le nom et les effets :"))
	try :
	
		if decision == 1 :
			new_molecule = quote(input("Entrez le nouveau nom de la molécule:"))
			sql="UPDATE Medicament SET nom_molecule = %s WHERE nom_molecule = %s;"%(new_molecule,nom_molecule)

		elif decision == 2 : 
			new_effets = quote(input("Entrez les nouveaux effets de la molécule:"))
			sql="UPDATE Medicament SET effets=%s WHERE nom_molecule = %s;"%(new_effets, nom_molecule)	
	 
		elif decision == 3 :
			new_molecule = quote(input("Entrez le nouveau nom de la molécule:"))
			new_effets = quote(input("Entrez les nouveaux effets de la molécule:"))
			sql="UPDATE Medicament SET nom_molecule = %s, effets=%s WHERE nom_molecule = %s;"%(new_molecule,new_effets, nom_molecule)

		cur.execute(sql)	
		conn.commit()
	
	except psycopg2.IntegrityError as e:
		conn.rollback()
		print("Message système :", e)
	
	print("Modification du médicament réalisée avec succès\n")

def afficher_medicaments(conn): #affiche tous les médicaments
	cur = conn.cursor()
	sql="SELECT * FROM Medicament"
	res=cur.fetchall()
	print("NOM \t EFFETS")
	for medicament in res :	
		print("%s \t %s \n\n"%(medicament[0],medicament[1]))

def afficher_non_autorise(conn): #affiche les espèces incompatibles avec un médicament donné
	cur = conn.cursor()
	nom_medicament = quote(input("Entrez le nom du médicament pour lequel vous voulez connaître les espèces interdites :"))
	
	try:
		sql="SELECT * FROM Espece EXCEPT SELECT espece, espece_taille FROM Est_autorise WHERE (Est_autorise.medicament = %s) ORDER BY categorie; "%(nom_medicament)
		cur.execute(sql)

		res = cur.fetchall()
		for espece in res:
			print("Un %s de taille %s ne peut pas prendre de %s\n"%(espece[0],espece[1],nom_medicament))


	except psycopg2.IntegrityError as e:
		conn.rollback()
		print("Message système :", e)

