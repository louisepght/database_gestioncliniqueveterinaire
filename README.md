# Projet_NF18 : Travail en équipe sur le sujet Veto

## Composition de l'équipe 1 du groupe D1

 * Daniel Duthoit 
 * Liza Al-Shikhley 
 * Louise Poughet
 * Sarah Deborde
 

## Rendu du projet

https://gitlab.utc.fr/sdeborde/projet_nf18


## Avertissement

Nous avons compris "fonctionnalités" comme une possibilité d'action pour un utilisateur.
Voici les fonctionnalités implémentées :
 * Gestion des clients:
	  *  création d'un client
	 * modification d'un client (nom, prénom, date de naissance et adresse)
	 * affichage de tous les clients
 * Gestion des patients:
	 * création d'un patient et de son dossier médical
	 * modification d'un patient (date de naissance, numéro de la puce, numéro du passeport et propriétaire)
	  * affichage des patients (tous les patients, une espèce et un propriétaire)
 * Gestion des médicaments
	  * création d'un médicament
	  * modification d'un médicament (effets)
	   * affichage des médicaments (tous les médicaments, espèces incompatibles avec un médicament)
 * Gestion du personnel de la clinique (vétérinaire ou assistant)
	  * création d'un membre du personnel
	  * modification d'un membre du personnel (nom, prenom, date de naissance et adresse)
	 * affichage des membres du personnel (tous les membres, un membre)
 * Génération du rapport d'activité:
	 * obtention du nombre de traitements prescrits pour une journée
	* classement des vétérinaires par nombre de patients


## Contenu du répertoire

 * Note de clarification.md : Dernière version de la note de clarification
 * UML.PLANTUML : code de génération du MCD en UML au format Plantuml
 * MLD.txt : MLD créé à partir de l'UML
 * script.sql : script de création des tables de la base de données
 * exemple_donnees.sql : script d'insertion des données de test
 * index.py : module python d'exécution de l'application
 * client.py : module python de gestion des clients
 * patient.py :module python de gestion des patients
 * medicaments.py : module python de gestion des médicaments
 * personnel.py : module python de gestion du personnel de la clinique
 * rapport_activite.py : module python générant des données statistiques


## Mise en place du projet sur votre ordinateur

1. Créez une base de données via PostgreSQL, dont vous serez le propriétaire. Si vous ne connaissez pas le mot de passe de postgres par défaut:
    * Utilisez la commande ```GRANT ALL PRIVILEGES to *votre nom d'utilisateur* ON *le nom de la base créée*;```
	* Puis, utilisez la commande ```GRANT USAGE, SELECT ALL ON SEQUENCES IN SCHEMA public TO *votre nom d'utilisateur* ;```
2. Exécutez sur votre base de données le script script.sql pour créer les tables, puis exemple_donnees.sql pour insérer les données


## Utilisation du projet

Pour lancer l'application Python:
1. Placez tous les scripts python dans le même répertoire.
2. Assurez-vous de rendre tous les scripts python exécutables.
3. Exécutez le script index.py avec Python3