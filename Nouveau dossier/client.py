#!/usr/bin/python3
import psycopg2
import datetime

def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'

def creer_client(conn) :
    cur = conn.cursor()
    try :
        _num_tel = quote(input("Entrez le numero de telephone du client."))        
        _nom = quote(input("Entrez le nom du client"))
        _prenom = quote(input("Entrez le prenom du client"))
        _annee = int(input("Entrez l'annee de naissance"))
        _mois = int(input("Entrez le mois de naissance"))
        _jour= int(input("Entrez le jour de naissance"))
        _date_de_naissance= quote(datetime.date(_annee, _mois, _jour))
        _adresse = quote(input("Entrez l'adresse du client."))
        
        sql_check = "SELECT num_telephone FROM Veterinaire UNION SELECT num_telephone FROM Assistant;"
        cur.execute(sql_check)
        res = cur.fetchall()
        if (_num_tel in res) :
            print("Vous avez entré des informations entrées pour un membre du personnel, veuillez réessayer\n")
            _num_tel = quote(input("Entrez le numero de telephone du client."))        
            _nom = quote(input("Entrez le nom du client"))
            _prenom = quote(input("Entrez le prenom du client"))
            _annee = int(input("Entrez l'annee de naissance"))
            _mois = int(input("Entrez le mois de naissance"))
            _jour= int(input("Entrez le jour de naissance"))
            _date_de_naissance= quote(datetime.date(_annee, _mois, _jour))
            _adresse = quote(input("Entrez l'adresse du client."))
			
        sql= "INSERT INTO Client(num_tel, nom, prenom, date_de_naissance, adresse) VALUES (%s, %s, %s, %s, %s);" % (_num_tel, _nom, _prenom, _date_de_naissance, _adresse)
        cur.execute(sql)
        conn.commit()
        print("Le client a bien été ajouté.")

    except psycopg2.IntegrityError as e :
        conn.rollback()
        print("Message système :", e)
        
    return _num_tel

def afficher_client(conn):
    cur = conn.cursor()
    sql = "SELECT * FROM Client;"
    cur.execute(sql)
    res = cur.fetchall()
    for resultat in res : 
            print(resultat)

def modifier_client(conn) :
    cur = conn.cursor()
    update = int(input("Que voulez vous mettre a jour?\n 1 num_tel, 2 nom, 3 prenom, 4 date_de_naissance, 5 adresse"))
    _searchnumtel = int(input("Entrez le numero de telephone appartenant au client a modifier."))

    if update == 1 :
        _num_tel = quote(input("Entrez le nouveau numero de telephone"))
        sql = "UPDATE Client SET num_tel = %i WHERE num_tel = %i" % (_num_tel, _searchnumtel)

    elif update == 2 :
        _nom = quote(input("Entrez le nouveau nom"))
        sql = "UPDATE Client SET nom = %s WHERE num_tel = %i; " % (_nom, _searchnumtel)

    elif update == 3 :
        _prenom = quote(input("Entrez le nouveau prenom"))
        sql = "UPDATE Client SET prenom = %s WHERE num_tel = %i;" % (_prenom, _searchnumtel)

    elif update == 4 :
        _annee = int(input("Entrez l'annee de naissance"))
        _mois = int(input("Entrez le mois de naissance"))
        _jour = int(input("Entrez le jour de naissance"))
        _date_de_naissance = quote(datetime.date(_annee, _mois, _jour))
        sql = "UPDATE Client SET date_de_naissance = %s WHERE num_tel = %i;" % (_date_de_naissance, _searchnumtel)

    elif update == 5 :
        _adresse = quote(input("Entrez la nouvelle adresse"))
        sql = "UPDATE Client SET adresse = %s WHERE num_tel = %i;" % (_adresse, _searchnumtel)

    cur.execute(sql)
    conn.commit()
