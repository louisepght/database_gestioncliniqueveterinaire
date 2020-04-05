#!/usr/bin/python3
import psycopg2
import os
from patient import *
from client import *
from personnel import *
from medicaments import *
from rapport_activite import *

def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'

def menu(conn):

    os.system("clear") #masque les précédentes étapes sur la console pour donner l'impression d'un nouvel affichage

    print("\t******************************************************\n\n")
    print("\t Bienvenue dans le gestionnaire de la clinique Veto ! \n\n")
    print("\t******************************************************\n")

    option = 0

#Exécution continue du gestionnaire, permet la réalisation de plusieurs taches à la suite.
    while (option < 6) :
        print("\n*** MENU PRINCIPAL : ***\n",
        " 1 - Gerer des patients \n",
        " 2 - Gerer des clients \n",
        " 3 - Gerer du personnel \n",
        " 4 - Gerer des medicaments \n",
        " 5 - Rapport d'activité \n",
        " 6 - Quitter \n")

        option=int(input("Que voulez-vous faire ? Tapez un nombre entre 1 et 5 et tapez 6 pour quitter :")) #adapte l'affichage du sous-menu selon ce que l'on souhaite traiter
        if option == 1 :
            menu_patient(conn)

        elif option == 2 :
            menu_client(conn)

        elif option == 3:
            menu_personnel(conn)

        elif option == 4 :
            menu_medicament(conn)

        elif option == 5 :
           menu_rapport(conn)


def menu_patient(conn):
    print("Vous avez choisi de gérer les patients de la clinique Veto. Que voulez-vous faire ?")
    choix = 0

    while (choix < 5) :
        print("\n\t* OPTIONS : * \n",
        "\t 1 - Creer un nouveau patient \n",
        "\t 2 - Modifier un patient existant \n",
        "\t 3 - Afficher le dossier medical d'un patient\n",
        "\t 4 - Afficher des patients \n",
        "\t 5 - Revenir au menu principal \n")

        choix=int(input("Que voulez-vous faire ? Tapez un nombre entre 1 et 4 et tapez 5 pour revenir en arriere : "))

        if choix == 1 :
            creer_patient(conn)

        elif choix == 2 :
            modifier_patient(conn)

        elif choix == 3 :
            afficher_dossier_patient(conn)

        elif choix == 4 :
            afficher_patient(conn)


def menu_client(conn):
    print("Vous avez choisi de gérer les clients de la clinique. Que voulez-vous faire ?")
    choix = 0
    while (choix < 3) :
        print("\n\t * OPTIONS : * \n",
        "\t 1 - Creer un nouveau client \n",
        "\t 2 - Modifier un client \n",
        "\t 3 - Afficher tous les clients \n",
        "\t 4 - Revenir au menu principal \n")
        choix=int(input("Tapez un nombre entre 1 et 2 ou tapez 3 pour revenir en arriere : "))

        if choix == 1 :
            creer_client(conn)

        elif choix == 2 :
            modifier_client(conn)

        elif choix == 3 :
            afficher_client(conn)




def menu_personnel(conn):

    print("Vous avez choisi de gérer le personnel. Que voulez-vous faire ?")
    choix = 0
    while (choix < 5) :
        print("\n \t * OPTIONS : * \n",
        "\t 1 - Creer un nouveau membre du personnel \n",
        "\t 2 - Modifier un membre du personnel \n",
        "\t 3 - Afficher un membre du personnel \n",
        "\t 4 - Afficher tout le personnel soignant \n",
        "\t 5 - Revenir au menu principal \n")
        choix=int(input("Tapez un nombre entre 1 et 4 ou tapez 5 pour revenir en arriere : "))

        if choix == 1 :
            creer_personnel(conn)

        elif choix == 2 :
            modifier_personnel(conn)

        elif choix == 3 :
            afficher_personnel(conn)
        
        elif choix == 4 :
            afficher_toutpersonnel(conn) 




def menu_medicament(conn):
    print("Vous avez choisi de gérer les patients de la clinique Veto. Que voulez-vous faire ?")
    choix = 0
    while (choix < 5) :
        print("\n\t * OPTIONS : * \n",
        "\t 1 - Ajouter un medicament a la liste \n",
        "\t 2 - Modifier un medicament \n",
        "\t 3 - Afficher tous les medicaments \n",
        "\t 4 - Afficher les espèces incompatibles avec un médicament\n",
        "\t 5 - Revenir au menu principal \n")
        choix=int(input("Que voulez-vous faire ? Tapez un nombre entre 1 et 4 et tapez 5 pour revenir en arriere : "))

        if choix == 1 :
            inserer_medicament(conn)

        elif choix == 2 :
            modifier_medicament(conn)

        elif choix == 3 :
            afficher_medicaments(conn)

        elif choix == 4 :
            afficher_non_autorise(conn)


def menu_rapport(conn):
    print("Vous souhaitez générer un rapport. Quelles informations souhaitez-vous ?")
    choix = 0
    while (choix < 3) :
        print("\n \t * OPTIONS : * \n",
        "\t 1 - Le nombre de traitements prescrits dans la journée \n",
        "\t 2 - Le nombre de patients par vétérinaire\n",
        "\t 3 - Revenir au menu principal \n")

        choix=int(input("Que voulez-vous faire ? Tapez un nombre entre 1 et 2 et tapez 3 pour revenir en arriere : "))

        if choix == 1 :
           nombre_traitement(conn)

        elif choix == 2 :
           sollicitation_veterinaires(conn)


def main ():
    print("\t------  PROJET NF18  ------ \n")
    print("\t------ TD1 GROUPE 01 ------ \n")
    print("Avant d'accéder au gestionnaire, veuillez vous connecter votre base de données\n")

#connexion à la base de données

    try:
        server = quote(input("Entrez le nom du serveur sur lequel se trouve la base de données : "))
        dbname = quote(input("Entrez le nom de votre base de données : "))
        username = quote(input("Entrez votre nom d'utilisateur : "))
        password = quote(input("Entrez votre mot de passe : "))

        conn=psycopg2.connect("host=%s dbname=%s user=%s password=%s"%(server,dbname,username,password))
   
        print("Vous êtes connecté à la base de données. Bienvenue %s ! \n"%(username))

        menu(conn)

    except psycopg2.Error as e:
        print("Echec de la connexion \n")
        print(e)
    
    conn.close() #fermeture de la session de connexion

#Exécution du programme
main()
