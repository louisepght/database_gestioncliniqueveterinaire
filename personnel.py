
#!/usr/bin/python3
import psycopg2
import datetime

def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'

def creer_personnel(conn) :  
	i = int(input("Etes vous sûr de vouloir gérer un membre du personnel? 1 pour oui, 0 pour non"))
	if i == 0 :  
		return
	if i == 1 : 
		personnel = int(input("Voulez vous ajouter un vétérinaire 1 ou un assistant 0?"))
		cur = conn.cursor()
		if personnel == 1 : 
			try :
				num_telephone = quote(input("Entrez le numéro de téléphone."))
				nom = quote(input("Entrez le nom."))
				prenom = quote(input("Entrez le prénom."))
				annee = int(input("Entrez l'année de naissance")) 
				mois = int(input("Entrez le mois de naissance")) 
				jour = int(input("Entrez le jour de naissance"))
				date_de_naissance = datetime.date(annee, mois, jour)
				adresse = quote(input("Entrez l'adresse."))
				sql = "INSERT INTO Veterinaire (num_telephone, nom, prenom, date_de_naissance, adresse) VALUES (%s, %s, %s, %s, %s)" % (num_telephone, nom, prenom, date_de_naissance, adresse)
				cur.execute(sql)
				conn.commit()
			except psycopg2.IntegrityError as e : 
				conn.rollback()
				print("Message système :", e)
			print("Le vétérinaire a bien été ajouté.")

		elif personnel == 0 : 
			try :
				num_telephone = quote(input("Entrez le numéro de téléphone."))
				nom = quote(input("Entrez le nom."))
				prenom = quote(input("Entrez le prénom."))
				annee = int(input("Entrez l'année de naissance")) 
				mois = int(input("Entrez le mois de naissance")) 
				jour = int(input("Entrez le jour de naissance"))
				date_de_naissance = datetime.date(annee, mois, jour)	
				adresse = quote(input("Entrez l'adresse."))
				sql = "INSERT INTO Veterinaire (num_telephone, nom, prenom, date_de_naissance, adresse) VALUES (%s, %s, %s, %s, %s)" % (num_telephone, nom, prenom, date_de_naissance, adresse)
				cur.execute(sql)
				conn.commit()
			except psycopg2.IntegrityError as e : 
				conn.rollback()
				print("Message système :", e)
			print("Le vétérinaire a bien été ajouté.")

		else : 
			print("Vous vous êtes trompé.")
			return gestion_personnel(conn)

def afficher_toutpersonnel(conn):
	cur = conn.cursor() 
	sql = "SELECT * FROM Personnel"
	cur.execute(sql)
	res = cur.fetchall() 
	i= 0
	while (res) : 
		print(res[i])
		i +=1

def afficher_personnel(conn):
	cur = conn.cursor() 
	searchnumtel = quote(input("Entrez le numéro de téléphone du membre àafficher."))
	sql = "SELECT * FROM Personnel WHERE num_telephone =%s" % (searchnumtel)
	cur.execute(sql)
	res = cur.fetchall() 
	for raw in res : 
		print(raw[0],raw[1],raw[3],raw[4],raw[5])

def supprimer_personnel(conn):
	cur = conn.cursor() 
	searchnumtel = quote(input("Entrez le numéro de téléphone du patient à supprimer."))
	sql = "DELETE FROM Personnel WHERE num_telephone = %s" % (searchnumtel)
	cur.execute(sql)
	conn.commit()

		
def modifier_personnel(conn) : 
	cur = conn.cursor() 
	personnel = int(input("Entrez 0 pour Veterinaire, ou 1 pour assistant"))
	searchnumtel = quote(intput("Entrez le numéro de téléphone du membre du personnel à modifier")
	if personnel == 0 : 
            
		update = int(input("Que voulez vous mettre à jour? 1 num_tel, 2 nom, 3 prenom, 4 date_de_naissance, 5 adresse"))
		if update == 1 : 
			num_tel = quote(input("Entrez le nouveau numéro de téléphone"))
			sql = "UPDATE Veterinaire SET num_telephone = %s WHERE num_tel = %s" % (num_tel, searchnumtel)

		elif update == 2 : 
			nom = quote(input("Entrez le nouveau nom"))
			sql = "UPDATE Veterinaire SET nom = %s WHERE num_tel = %s" %(nom, searchnumtel)
		elif update == 3 : 
			prenom = quote(input("Entrez le nouveau prénom"))
			sql = "UPDATE Veterinaire SET prenom = %s WHERE num_tel = %s " %(prenom, searchnumtel)
		elif update == 4 : 
			annee = int(input("Entrez l'année de naissance")) 
			mois = int(input("Entrez le mois de naissance")) 
			jour = int(input("Entrez le jour de naissance"))
			date_de_naissance = datetime.date(annee, mois, jour)
			sql = "UPDATE Veterinaire SET date_de_naissance =%s WHERE num_tel =%s" %(date_de_naissance, searchnumtel)
		elif update == 5 : 
			adresse = quote(input("Entrez la nouvelle adresse"))
			sql = "UPDATE Veterinaire SET adresse = %s WHERE num_tel =%s" %(adresse, searchnumtel)
		cur.execute(sql)
		conn.commit()

	elif personnel == 1 : 
		update = int(input("Que voulez vous mettre à jour? \n 1 num_tel, 2 nom, 3 prenom, 4 date_de_naissance, 5 adresse") 
		if update == 1 : 
			num_tel = quote(input("Entrez le nouveau numéro de téléphone"))
			sql = "UPDATE Assistant SET num_telephone = %s WHERE num_tel = %s" % (num_tel, searchnumtel)

		elif update == 2 : 
			nom = quote(input("Entrez le nouveau nom"))
			sql = "UPDATE Assistant SET nom = %s WHERE num_tel = %s" % (nom, searchnumtel)

		elif update == 3 : 
			prenom = quote(input("Entrez le nouveau prénom"))
			sql = "UPDATE Assistant SET prenom = %s WHERE num_tel =%s" % (prenom, searchnumtel)

		elif update == 4 : 
			annee = int(input("Entrez l'année de naissance")) 
			mois = int(input("Entrez le mois de naissance")) 
			jour = int(input("Entrez le jour de naissance"))
			date_de_naissance = datetime.date(annee, mois, jour)
			sql = "UPDATE Assistant SET date_de_naissance =%s WHERE num_tel =%s " % (date_de_naissance,searchnumtel)

		elif update == 5 : 
			adresse = quote(input("Entrez la nouvelle adresse"))
			sql = "UPDATE Assistant SET adresse = %s WHERE num_tel =%s "%(adresse, searchnumtel)

		cur.execute(sql)
		conn.commit()

	else : 
		print("Vous vous êtes trompé") 
		return modifier_personnel(conn)























