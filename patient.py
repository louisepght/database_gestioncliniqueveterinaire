import psycopg2
import datetime

import client

def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'

def afficher_patient(conn): 
    i = int(input("Sur quel critère voulez-vous afficher les patients? 1 si vous voulez afficher tous les patients, 2 si vous voulez afficher une espèce en particulier, 3 si vous voulez affichier les patients d'un proprietaire")) 
    if i == 1:
		try:
			cur = conn.cursor()
			sql = "SELECT * FROM Patient"
	if i == 2:
		try:
			espece = quote(input("Entrez le nom d'espece"))
			cur = conn.cursor()
			sql = "SELECT * FROM Patient WHERE espece = %s" % (espece)
	if i == 3:
		try:
			proprietaire = quote(input("Entrez le nom d'un proprietaire"))
			cur = conn.cursor()
			sql = "SELECT * FROM Patient WHERE proprietaire = %s" % (proprietaire)
    cur.execute(sql)
    res = cur.fetchall() 
    i= 0
    while res : 
        print(res[i])
        i +=1

def afficher_dossier_patient(conn):
	i = int(input("Entrez le numéro de son dossier médical")) 
	try:
		cur = conn.cursor()
		sql_traitement = "SELECT * FROM Traitement WHERE dossier = %s" (dossier)
		sql_consultation = "SELECT * FROM Consultation WHERE dossier = %s" (dossier)
		sql_taille = "SELECT * FROM Taille WHERE dossier_medical = %s" (dossier)
		sql_poids = "SELECT * FROM Poids WHERE dossier_medical = %s" (dossier)
		sql_analyses = "SELECT * FROM Analyses WHERE dossier_medical = %s" (dossier)
    		cur.execute(sql_traitement)
    		res = cur.fetchall() 
    		i= 0
    		while res : 
        		print(res[i])
        		i +=1
    		cur.execute(sql_consultation)
    		res = cur.fetchall() 
    		i= 0
    		while res : 
        		print(res[i])
        		i +=1
   		cur.execute(sql_taille)
    		res = cur.fetchall() 
    		i= 0
    		while res : 
        		print(res[i])
        		i +=1
    		cur.execute(sql_poids)
    		res = cur.fetchall() 
    		i= 0
    		while res : 
        		print(res[i])
        		i +=1
    		cur.execute(sql_analyses)
    		res = cur.fetchall() 
    		i= 0
    		while res : 
        		print(res[i])
        		i +=1

def creer_patient(conn) :  
	i = int(input("Etes vous sûr de vouloir créer un patient? 1 pour oui, 0 pour non"))
	if i == 0 : 
        return
	if i == 1 : 
		try :
		ii = int(input("Le propriétaire est-il déjà client de la clinique ?1 pour oui, 0 pour non"))
		if ii == 0:
			creer_client(conn)
		if i == 1 :
			nom? = quote(input("Entrez le nom du patient"))
			date_naissance = "inconnue"
			espece = quote(input("Entrez l'espèce à laquelle appartient le patient"))
			espece_taille = quote(input("Entrez la taille de l'espèce à laquelle appartient le patient"))
			sql = "INSERT INTO Patient(idp?,? ?nom?,? date_naissance?,? ?espece, espece_taille?) VALUES (default, %s, %s, %s, %s)" % (?nom?,? ??date_naissance?,? espece, espece_taille?)
		cur.execute(sql)
		conn.commit(à
        except psycopg2.IntegrityError as e : 
            conn.rollback()
            print("Message système :", e)

        print("Le patient a bien été ajouté.")

    else : 
        print("Vous vous êtes trompé.")
        return creer_patient(conn)


def modifier_patient(conn) : 
	cur = conn.cursor() 
	idp = int(input("Entrez le numéro d'identifiant du patient à modifier."))
	update = int(input("Que voulez vous mettre à jour?\n 1 date_naissance, 2 num_puce, 3 num_passeport, 4 propriétaire"))
    
	if update == 1 : 
		date_naissance = quote(input("Entrez la nouvelle date de naissance"))
		try:
			sql = "UPDATE Patient SET date_naissance = %s WHERE idp = %i" % (date_naissance, idp)
		except psycopg2.IntegrityError as e : 
			conn.rollback()
			print("Message système :", e)

	elif update == 2 : 
        	num_puce = quote(input("Entrez le nouveau numéro de puce"))
        	try:
			sql = "UPDATE Patien SET num_puce = %s WHERE idp = %i" % (num_puce, idp)
		except psycopg2.IntegrityError as e : 
            	conn.rollback()
            	print("Message système :", e)
    
	elif update == 3 : 
		num_passeport = quote(input("Entrez le nouveau numéro de passeport"))
		try:
			sql = "UPDATE Patient SET num_passeport = %s WHERE idp = %i" % (num_passeport, idp)
		except psycopg2.IntegrityError as e : 
            	conn.rollback()
            	print("Message système :", e)

	elif update == 4 : 
		proprietaire = int(input("Entrez le nouveau numéro de téléphone du propriétaire"))
        	try:
			sql = "UPDATE Patient SET proprietaire = %s WHERE idp = %i" % (proprietaire, idp)
		except psycopg2.IntegrityError as e : 
            	conn.rollback()
            	print("Message système :", e)
		
    	cur.execute(sql)
    	conn.commit()