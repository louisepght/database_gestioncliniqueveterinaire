#!/usr/bin/python3
import psycopg2
import datetime
from client import creer_client

def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'

def afficher_patient(conn): 
    cur = conn.cursor()
    i = int(input("Sur quel critère voulez-vous afficher les patients? \n 1 pour tous les patients, 2 pour une espèce en particulier, 3 pour les patients d'un proprietaire : ")) 
    if i == 1:
       try:           
            sql = "SELECT * FROM Patient;"
       except psycopg2.IntegrityError as e : 
            conn.rollback()
            print("Message système :", e)

    elif i == 2:
        
        try:
            _espece = quote(input("Entrez le nom d'espece : "))
            sql = "SELECT * FROM Patient WHERE espece = %s;" % (_espece)
        
        except psycopg2.IntegrityError as e : 
            conn.rollback()
            print("Message système :", e)

    elif i == 3:
        try:
            _proprietaire = quote(input("Entrez le nom d'un proprietaire : "))
            sql = "SELECT * FROM Patient WHERE proprietaire = %s;" % (_proprietaire)
        except psycopg2.IntegrityError as e : 
            conn.rollback()
            print("Message système :", e)
    
    cur.execute(sql)
    res = cur.fetchall() 
    for resultat in res : 
        print(resultat)
    

def afficher_dossier_patient(conn):
    _dossier = quote(input("Entrez l'identifiant du dossier médical : ")) 
    sql_traitement = "SELECT * FROM Traitement WHERE dossier = %s;"%(_dossier)
    sql_consultation = "SELECT * FROM Consultation WHERE dossier = %s;"%(_dossier)
    sql_taille = "SELECT * FROM Taille WHERE dossier_medical = %s;"%(_dossier)
    sql_poids = "SELECT * FROM Poids WHERE dossier_medical = %s;"%(_dossier)
    sql_analyses = "SELECT * FROM Analyses WHERE dossier_medical = %s;"%(_dossier)
    
    cur = conn.cursor()
    
    try:
        cur.execute(sql_traitement)
        res = cur.fetchall() 
        for resultat in res : 
            print(resultat)
            
    except psycopg2.IntegrityError as e : 
        conn.rollback()
        print("Message système :", e)

    try:
        cur.execute(sql_consultation)
        res = cur.fetchall() 
        for resultat in res : 
            print(resultat)
            
    except psycopg2.IntegrityError as e : 
        conn.rollback()
        print("Message système :", e)  

    try:
        cur.execute(sql_taille)
        res = cur.fetchall() 
        for resultat in res : 
            print(resultat)
            
    except psycopg2.IntegrityError as e : 
        conn.rollback()
        print("Message système :", e)  

    try:
        cur.execute(sql_poids)
        res = cur.fetchall() 
        for resultat in res : 
            print(resultat)
            
    except psycopg2.IntegrityError as e : 
        conn.rollback()
        print("Message système :", e)  

    try:
        cur.execute(sql_analyses)
        res = cur.fetchall() 
        for resultat in res : 
            print(resultat)
         
    except psycopg2.IntegrityError as e : 
        conn.rollback()
        print("Message système :", e)  


def creer_patient(conn) :  
    i = int(input("Votre patient a-t-il un propriétaire ? 1 pour oui, 0 pour non : "))
    cur = conn.cursor()
    _nom = quote(input("Entrez le nom du patient : "))
    _date_naissance = quote(input("Entrez la date naissance du patient, l'année de naissance ou inconnue : "))
    _espece = quote(input("Entrez l'espèce à laquelle appartient le patient : "))
    _espece_taille = quote(input("Entrez la taille de l'espèce à laquelle appartient le patient : "))
    
    if i == 0 : 
        sql = "INSERT INTO Patient(nom, date_naissance, espece, espece_taille) VALUES (%s, %s, %s, %s);" % (_nom, _date_naissance, _espece, _espece_taille)
    if i == 1 : 
        try :
            ii = int(input("Le propriétaire est-il déjà client de la clinique ? 1 pour oui, 0 pour non : "))
            if ii == 0:
                _tel = creer_client(conn)   
            else :   
                _tel = quote(input("Quel est le numero de téléphone du client ? "))
			
            sql = "INSERT INTO Patient(nom, date_naissance, espece, espece_taille,proprietaire) VALUES (%s, %s, %s, %s, %s);" % (_nom, _date_naissance, _espece, _espece_taille,_tel)
            cur.execute(sql)
            
            #On récupère l'ID du nouveau patient            
            sql_ID = "SELECT MAX(IdP) FROM Patient;" 
            cur.execute(sql_ID)
            res = cur.fetchone()
            _numero = int(res[0])
            _idP = quote(_numero)
			
            #On initialise un nouveau dossier avec l'ID du nouveau patient
            sql_num = "INSERT INTO Dossier_medical VALUES (%i);"%(_numero)
            cur.execute(sql_num)
			
            #On ajoute le numéro de dossier
            sql_update = "UPDATE Patient SET dossier_medical = %i WHERE IdP=%s;"%(_numero, _idP) #On ajoute le numéro de dossier
            cur.execute(sql_update)
			
            conn.commit()
            print("Le patient a bien été ajouté.")
            
        except psycopg2.IntegrityError as e : 
            conn.rollback()
            print("Message système :", e)

    else : 
        print("Vous vous êtes trompé.")
        return creer_patient(conn)


def modifier_patient(conn) : 
    cur = conn.cursor() 
    _idp = quote(input("Entrez le numéro d'identifiant du patient à modifier : "))
    update = int(input("Que voulez vous mettre à jour?\n 1 date_naissance, 2 num_puce, 3 num_passeport, 4 propriétaire : "))

    if update == 1 : 
        _date_naissance = quote(input("Entrez la nouvelle date de naissance : "))
        try:
            sql = "UPDATE Patient SET date_naissance = %s WHERE idp = %s;" % (_date_naissance, _idp)
        except psycopg2.IntegrityError as e : 
            conn.rollback()
            print("Message système :", e)

    elif update == 2 : 
        _num_puce = quote(input("Entrez le nouveau numéro de puce : "))
        try:
            sql = "UPDATE Patient SET num_puce = %s WHERE idp = %s;" % (_num_puce, _idp)
        except psycopg2.IntegrityError as e : 
            conn.rollback()
            print("Message système :", e)

    elif update == 3 : 
        _num_passeport = quote(input("Entrez le nouveau numéro de passeport : "))
        try:
            sql = "UPDATE Patient SET num_passeport = %s WHERE idp = %s;" % (_num_passeport, _idp)
        except psycopg2.IntegrityError as e : 
            conn.rollback()
            print("Message système :", e)

    elif update == 4 : 
        _proprietaire = quote(input("Entrez le nouveau numéro de téléphone du propriétaire : "))
        try:
            sql = "UPDATE Patient SET proprietaire = %s WHERE idp = %s;" % (_proprietaire, _idp)
        except psycopg2.IntegrityError as e : 
            conn.rollback()
            print("Message système :", e)

    cur.execute(sql)
    conn.commit()


