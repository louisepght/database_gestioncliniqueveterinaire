import psycopg2
import datetime

import client

def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'

def afficher_patient(conn): 
    i = int(input("Sur quel crit�re voulez-vous afficher les patients? 1 si vous voulez afficher tous les patients, 2 si vous voulez afficher une esp�ce en particulier, 3 si vous voulez affichier les patients d'un proprietaire")) 
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
	i = int(input("Entrez le num�ro de son dossier m�dical")) 
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
	i = int(input("Etes vous s�r de vouloir cr�er un patient? 1 pour oui, 0 pour non"))
	if i == 0 : 
        return
	if i == 1 : 
		try :
		ii = int(input("Le propri�taire est-il d�j� client de la clinique ?1 pour oui, 0 pour non"))
		if ii == 0:
			creer_client(conn)
		if i == 1 :
			nom? = quote(input("Entrez le nom du patient"))
			date_naissance = "inconnue"
			espece = quote(input("Entrez l'esp�ce � laquelle appartient le patient"))
			espece_taille = quote(input("Entrez la taille de l'esp�ce � laquelle appartient le patient"))
			sql = "INSERT INTO Patient(idp?,? ?nom?,? date_naissance?,? ?espece, espece_taille?) VALUES (default, %s, %s, %s, %s)" % (?nom?,? ??date_naissance?,? espece, espece_taille?)
		cur.execute(sql)
		conn.commit(�
        except psycopg2.IntegrityError as e : 
            conn.rollback()
            print("Message syst�me :", e)

        print("Le patient a bien �t� ajout�.")

    else : 
        print("Vous vous �tes tromp�.")
        return creer_patient(conn)


def modifier_patient(conn) : 
	cur = conn.cursor() 
	idp = int(input("Entrez le num�ro d'identifiant du patient � modifier."))
	update = int(input("Que voulez vous mettre � jour?\n 1 date_naissance, 2 num_puce, 3 num_passeport, 4 propri�taire"))
    
	if update == 1 : 
		date_naissance = quote(input("Entrez la nouvelle date de naissance"))
		try:
			sql = "UPDATE Patient SET date_naissance = %s WHERE idp = %i" % (date_naissance, idp)
		except psycopg2.IntegrityError as e : 
			conn.rollback()
			print("Message syst�me :", e)

	elif update == 2 : 
        	num_puce = quote(input("Entrez le nouveau num�ro de puce"))
        	try:
			sql = "UPDATE Patien SET num_puce = %s WHERE idp = %i" % (num_puce, idp)
		except psycopg2.IntegrityError as e : 
            	conn.rollback()
            	print("Message syst�me :", e)
    
	elif update == 3 : 
		num_passeport = quote(input("Entrez le nouveau num�ro de passeport"))
		try:
			sql = "UPDATE Patient SET num_passeport = %s WHERE idp = %i" % (num_passeport, idp)
		except psycopg2.IntegrityError as e : 
            	conn.rollback()
            	print("Message syst�me :", e)

	elif update == 4 : 
		proprietaire = int(input("Entrez le nouveau num�ro de t�l�phone du propri�taire"))
        	try:
			sql = "UPDATE Patient SET proprietaire = %s WHERE idp = %i" % (proprietaire, idp)
		except psycopg2.IntegrityError as e : 
            	conn.rollback()
            	print("Message syst�me :", e)
		
    	cur.execute(sql)
    	conn.commit()