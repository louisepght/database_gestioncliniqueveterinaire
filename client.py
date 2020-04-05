#!/usr/bin/python3
import psycopg2
import datetime

def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'

def creer_client(conn) :
	i = int(input("Etes vous sur de vouloir creer un client? 1 pour oui, 0 pour non"))
	if i == 0 :
		return
	if i == 1 :
        	try :
			num_tel = quote(input("Entrez le numero de telephone du client."))
			nom = quote(input("Entrez le nom du client"))
			prenom = quote(input("Entrez le prenom du client"))
			annee = int(input("Entrez l'annee de naissance"))
			mois = int(input("Entrez le mois de naissance"))
			jour= int(input("Entrez le jour de naissance"))
			date_de_naissance= datetime.date(annee, mois, jour)
			adresse = quote(input("Entrez l'adresse du client."))

	    		sql= "INSERT INTO Client(num_tel, nom, prenom, date_de_naissance, adresse) VALUES (%i, %s, %s, %i, %i, %i, %s, %s)" % (num_tel, nom, prenom, date_de_naissance, adresse)
	    		cur.execute(sql)
	    		conn.commit()

		except psycopg2.IntegrityError as e :
			conn.rollback()
			print("Message système :", e)

		print("Le client a bien ete ajoute.")

	else :
		print("Vous vous etes trompe.")
		return creer_client(conn)

def afficher_client(conn):
	cur = conn.cursor()
	sql = "SELECT * FROM Client"
	cur.execute(sql)
	res = cur.fetchall()
	i= 0
	while res :
		print(res[i])
		i +=1

def modifier_client(conn) :
	cur = conn.cursor()
	update = int(input("Que voulez vous mettre a jour?\n 1 num_tel, 2 nom, 3 prenom, 4 date_de_naissance, 5 adresse"))
	searchnumtel = int(input("Entrez le numero de telephone appartenant au client a modifier."))

	if update == 1 :
		num_tel = quote(input("Entrez le nouveau numero de telephone"))
		sql = "UPDATE Client SET num_tel = %i WHERE num_tel = %i" % (num_tel, searchnumtel)

	elif update == 2 :
		nom = quote(input("Entrez le nouveau nom"))
		sql = "UPDATE Client SET nom = %s WHERE num_tel = %i " % (nom, searchnumtel)

	elif update == 3 :
		prenom = quote(input("Entrez le nouveau prenom"))
		sql = "UPDATE Client SET prenom = %s WHERE num_tel = %i" % (prenom, searchnumtel)

	elif update == 4 :
		annee = int(input("Entrez l'annee de naissance"))
        	mois = int(input("Entrez le mois de naissance"))
        	jour = int(input("Entrez le jour de naissance"))
		date_de_naissance = datetime.date(annee, mois, jour)
		sql = "UPDATE Client SET date_de_naissance = %s WHERE num_tel = %i" % (date_de_naissance, searchnumtel)

	elif update == 5 :
		adresse = quote(input("Entrez la nouvelle adresse"))
		sql = "UPDATE Client SET adresse = %s WHERE num_tel = %i" % (adresse,nsearchnumtel)

	cur.execute(sql)
    	conn.commit()
