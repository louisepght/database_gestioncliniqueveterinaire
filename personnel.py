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
                _num_telephone = quote(input("Entrez le numéro de téléphone."))
                _nom = quote(input("Entrez le nom."))
                _prenom = quote(input("Entrez le prénom."))
                _annee = quote(input("Entrez l'année de naissance")) 
                _mois = quote(input("Entrez le mois de naissance")) 
                _jour = quote(input("Entrez le jour de naissance"))
                _date_de_naissance = quote(datetime.date(_annee, _mois, _jour))
                _adresse = quote(input("Entrez l'adresse."))
                sql = "INSERT INTO Veterinaire (num_telephone, nom, prenom, date_de_naissance, adresse) VALUES (%s, %s, %s, %s, %s);" % (_num_telephone, _nom, _prenom, _date_de_naissance, _adresse)
                cur.execute(sql)
                conn.commit()
            except psycopg2.IntegrityError as e : 
                conn.rollback()
                print("Message système :", e)
            
            print("Le vétérinaire a bien été ajouté.")

        elif personnel == 0 : 
            try :
                _num_telephone = quote(input("Entrez le numéro de téléphone."))
                _nom = quote(input("Entrez le nom."))
                _prenom = quote(input("Entrez le prénom."))
                _annee = int(input("Entrez l'année de naissance")) 
                _mois = int(input("Entrez le mois de naissance")) 
                _jour = int(input("Entrez le jour de naissance"))
                _date_de_naissance = quote(datetime.date(_annee, _mois, _jour))
                _adresse = quote(input("Entrez l'adresse."))
                sql = "INSERT INTO Veterinaire (num_telephone, nom, prenom, date_de_naissance, adresse) VALUES (%s, %s, %s, %s, %s);" % (_num_telephone, _nom, _prenom, _date_de_naissance, _adresse)
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
    print("\n Liste des vétérinaires : \n")
    sql = "SELECT * FROM Veterinaire;"
    cur.execute(sql)
    res = cur.fetchall() 
    for resultat in res : 
            print(resultat)
    
    print("\n Liste des assistants : \n")
    sql = "SELECT * FROM Assistant;"
    cur.execute(sql)
    res = cur.fetchall() 
    for resultat in res : 
            print(resultat)

def afficher_personnel(conn):
    cur = conn.cursor() 
    _searchnumtel = quote(input("Entrez le numéro de téléphone du membre à afficher."))
    _table = input("Est-ce un vétérinaire (Veterinaire) ou un assistant (Assistant) ?")
    sql = "SELECT * FROM %s WHERE num_telephone =%s;" % (_table, _searchnumtel)
    cur.execute(sql)
    res = cur.fetchall() 
    for raw in res : 
        print(raw[0],raw[1],raw[3],raw[4],raw[5])

def supprimer_personnel(conn):
    cur = conn.cursor() 
    try:
        _searchnumtel = quote(input("Entrez le numéro de téléphone du patient à supprimer."))
        _table = input("Est-ce un vétérinaire (Veterinaire) ou un assistant (Assistant) ?")
        sql = "DELETE FROM %s WHERE num_telephone =%s;" % (_table, _searchnumtel)
        cur.execute(sql)
        conn.commit()
    except psycopg2.IntegrityError as e : 
        conn.rollback()
        print("Message système :", e)
 

def modifier_personnel(conn) : 
    cur = conn.cursor() 
    personnel = int(input("Entrez 0 pour Veterinaire, ou 1 pour assistant"))
    _searchnumtel = quote(input("Entrez le numéro de téléphone du membre du personnel à modifier"))
    if personnel == 0 :
        update = int(input("Que voulez vous mettre à jour? 1 nom, 2 prenom, 3 date_de_naissance, 4 adresse"))
        
        if update == 1 : 
            _nom = quote(input("Entrez le nouveau nom"))
            sql = "UPDATE Veterinaire SET nom = %s WHERE num_tel = %s;" %(_nom, _searchnumtel)

        elif update == 2 : 
            _prenom = quote(input("Entrez le nouveau prénom"))
            sql = "UPDATE Veterinaire SET prenom = %s WHERE num_tel = %s; " %(_prenom, _searchnumtel)

        elif update == 3 : 
            _annee = quote(input("Entrez l'année de naissance")) 
            _mois = quote(input("Entrez le mois de naissance"))
            _jour = quote(input("Entrez le jour de naissance"))
            _date_de_naissance = quote(datetime.date(_annee, _mois, _jour))
            sql = "UPDATE Veterinaire SET date_de_naissance =%s WHERE num_tel =%s;" %(_date_de_naissance, _searchnumtel)
       
        elif update == 4 : 
            _adresse = quote(input("Entrez la nouvelle adresse"))
            sql = "UPDATE Veterinaire SET adresse = %s WHERE num_tel =%s;" %(_adresse, _searchnumtel)
            cur.execute(sql)
            conn.commit()

    elif personnel == 1 : 
        update = int(input("Que voulez vous mettre à jour? \n 1 nom, 2 prenom, 3 date_de_naissance, 4 adresse"))

        if update == 1 : 
            _nom = quote(input("Entrez le nouveau nom"))
            sql = "UPDATE Assistant SET nom = %s WHERE num_tel = %s;" % (_nom, _searchnumtel)

        elif update == 2 : 
            _prenom = quote(input("Entrez le nouveau prénom"))
            sql = "UPDATE Assistant SET prenom = %s WHERE num_tel =%s;" % (_prenom, _searchnumtel)

        elif update == 3 : 
            _annee = quote(input("Entrez l'année de naissance")) 
            _mois = quote(input("Entrez le mois de naissance"))
            _jour = quote(input("Entrez le jour de naissance"))
            _date_de_naissance = quote(datetime.date(_annee, _mois, _jour))
            sql = "UPDATE Assistant SET date_de_naissance =%s WHERE num_tel =%s ;" % (_date_de_naissance, _searchnumtel)

        elif update == 4 : 
            _adresse = quote(input("Entrez la nouvelle adresse"))
            sql = "UPDATE Assistant SET adresse = %s WHERE num_tel =%s ;"%(_adresse, _searchnumtel)

        cur.execute(sql)
        conn.commit()

    else : 
        print("Vous vous êtes trompé") 
        return modifier_personnel(conn)
