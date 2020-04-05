# Projet_NF18 : Travail en équipe sur le sujet Veto

## Composition de l'équipe 1 du groupe D1</h1>

 * Daniel Duthoit 
 * Liza Al-Shikhley 
 * Louise Poughet
 * Sarah Deborde
 

https://gitlab.utc.fr/sdeborde/projet_nf18

## Avertissement
Nous avons compris fonctionnalités comme une possibilité d'action pour un utilisateur.
Voici les fonctionallités implémentées :
* Créer un client
* Créer un patient
* Créer un médicament
* Créer un membre du personnel (vétérinaire ou assistant)
* Afficher un client
* Afficher le dossier médical d'un patient
*

## Mise en place du projet sur votre ordinateur
1. Créez une base de données via PostgreSQL, dont vous serez le propriétaire.
	a. Si vous ne connaissez pas le mot de passe de postgres par défaut, utilisez la commande GRANT ALL PRIVILEGES to *votre nom d'utilisateur* ON *le nom de la base créée*;)
	b. Puis, utilisez la commande GRANT USAGE, SELECT ALL ON SEQUENCES IN SCHEMA public TO *votre nom d'utilisateur* ;
2. Exécutez sur votre base de données le script script.sql pour créer les tables, puis exemple_donnees.sql pour insérer les données
3. Exécutez index.py avec python3

### Utilisation du projet
Pour lancer l'application Python:
1. Placez tous les scripts python dans le même répertoire.
2. Assurez-vous de rendre tous les scripts exécutables.
3. Exécutez le script index.py 
