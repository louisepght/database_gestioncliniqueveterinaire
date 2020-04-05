#!/usr/bin/python3
import psycopg2
import datetime


def nombre_traitement(conn) : #nombre de traitements prescrits dans une journée
	cur = conn.cursor()
	print("Voulez-vous connaître le nombre de traitements prescrits aujourd'hui ou à une autre date ?\n")
	choix_date = int(input("Tapez 1 pour aujourd'hui, taper 2 pour une autre date "))
	while ((choix_date<1) and (choix_date>2)):
		choix_date = int(input("Veuillez réessayer. Tapez 1 pour aujourd'hui, taper 2 pour une autre date "))
	if choix_date == 1 :
		sql = "SELECT COUNT(*) as Nombre_traitements_prescrit FROM Traitement WHERE date_heure_saisie::date = current_date;"
		cur.execute(sql)
	
	elif choix_date == 2 :
		annee = int(input("Entrez l'année"))
		mois = int(input("Entrez le mois"))
		jour = int(input("Entrez le jour"))
		date = datetime.date(annee, mois, jour)
		sql = "SELECT COUNT(*) as Nombre_traitements_prescrit FROM Traitement WHERE date_heure_saisie::date = %s::date;"%(date)
	

def sollicitation_veterinaires(conn): #classement des vétérinaires avec le plus de patients 
	cur = conn.cursor()
	sql = "SELECT veterinaire, COUNT(*) as Nombre_patients FROM Suivi_veterinaire JOIN Veterinaire ON Suivi_veterinaire.veterinaire = Veterinaire.num_telephone GROUP BY Suivi_veterinaire.veterinaire ORDER BY Nombre_patients DESC ;"
	cur.execute(sql)
	res = cur.fetchall()
	print("Vétérinaire \t Nombre de patients\n")
	for resultat in res :
		print("%s \t %s"%(resultat[1], resultat[2]))
	
