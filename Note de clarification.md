# Note de clarification

 ## Contexte et objectifs

La clinique vétérinaire Veto nous demande de mettre en place un système capable de gérer les patients, les clients, le personnel soignant et les médicaments administrés. Cette gestion sera assurée par l’administrateur de la clinique pour ajouter, modifier, rechercher ou supprimer les informations relatives aux patients, aux clients, au personnel et aux médicaments administrés.

Ces informations seront présentées sous la forme d’une base de données, dans laquelle elles seront stockées. Nous livrerons une application capable de les manipuler de manière sûre, fiable et intuitive : il s’agit, entre autres, d’une interface qui se positionne comme intermédiaire entre la base de données et les utilisateurs. L’interaction aura lieu à travers des requêtes, qui servent à ajouter, modifier, supprimer ou accéder aux informations présentes dans la base de données. De même, les requêtes permettront la production de rapport d’activités de la clinique et de données statistiques telles que le nombre de traitements ou de procédures réalisées dans la clinique, les quantités de médicaments consommés ou bien des statistiques basées sur les espèces d’animaux traités.

Dans ce document, nous désignerons par “personnes” les clients et le personnel. Nous considérons que l’administrateur et le gestionnaire de la clinique sont la même personne.

Par ailleurs, si une caractéristique n’est pas mentionnée explicitement comme optionnelle, elle est considérée comme étant par défaut obligatoire.

## Acteurs du projet

Le client est la clinique vétérinaire Veto dont M. Youcef AMAROUCHE est le représentant.

La maîtrise d’oeuvre est réalisée par notre équipe, composée de 4 membres :

-   AL-SHIKHLEY Liza - GI02 (formation continue)
    
-   DEBORDE Sarah - GI03
    
-   DUTHOIT Daniel - GU04
    
-   POUGHET Louise - GI01
    

## Livrables de l’étude

Dans le cadre de ce projet, plusieurs livrables sont attendus. Ceux-ci sont jalonnés sur deux phases de rendus :

**Phase 0 :**

-   Le fichier README (avec les noms des membres du groupe), au format markdown, remis en amont du projet le 21 mars 2020
    

**Première phase :**

-   **Premier jalon (28 mars 2020) : Analyse du besoin de l’utilisateur**

	-  La note de clarification au format markdown


-   **Deuxième jalon (04 avril 2020) : Conception et développement**
    
	-   Le modèle conceptuel de données, sous la forme d’un diagramme UML
    
	-   Le modèle logique de données relationnel
    
	-   La base de données, comprenant les tables, les données de test et les questions attendues
    
	-   L’application
    

**Deuxième phase :**

La deuxième phase de notre projet vise à perfectionner les précédents livrables. Il s’agira de corriger les erreurs relevées lors de la première phase, d'intégrer de nouvelles fonctions et d’optimiser.

-   **Premier jalon (13 juin 2020) :**

	-   La nouvelle note de clarification



-   **Deuxième jalon (20 juin 2020) : finalisation de la conception**

	-   Le modèle conceptuel de données
    
	-   Le modèle logique de données relationnel
    
	-   La base de données, comprenant tables et vues, données de test, questions attendues (vues)
    
	-   L’application finale
    

## Contraintes

* Toute livraison réalisée devra être **fonctionnelle et compatible** avec l’environnement de travail du client. Ainsi, le code devra être compatible avec la version de PostgreSQL installée sur le parc informatique de l’UTC.

* L’application doit être codée en Python.

## Risques

Les risques suivants seront à considérer tout au long du projet afin de ne pas nuire à sa réalisation :

-   Mauvaise maîtrise des outils informatiques
    
-   Manque d’aisance avec les langages utilisés
    
-   Imprévus matériels comme une panne
    
-   Mauvaise organisation
    
-   Mauvaise modélisation du problème
    

## Système d’information et de communication

Le cahier des charges déposé par la clinique Veto est présentée sur le site libre-cours.net.

Toute livraison aura lieu sous la forme d’une URL vers le dernier commit Git sur le répertoire du projet, hébergé sur le GitLab de l’Université de Technologie de Compiègne (UTC). Le projet sera consultable dans son intégralité à l’URL suivante : [https://gitlab.utc.fr/sdeborde/projet_nf18](https://gitlab.utc.fr/sdeborde/projet_nf18)

  

La communication avec le représentant de la clinique se fera par courriel ou bien sur Mattermost, avec tous les membres de l’équipe en mention ou en copie.

  

L’architecture du projet repose sur plusieurs dispositifs :

-   La distribution Ubuntu du système d’exploitation Linux, disponible sur les postes du l’UTC et sur nos ordinateurs personnels en dual-boot ou sur une machine virtuelle
    
-   Le système de gestion de base de données PostgreSQL
    
-   Le langage de programmation Python pour notre application
    
-   Le langage Plantuml pour la modélisation conceptuelle des données
    

En interne, l’équipe communiquera par le biais de Mattermost, avec des réunions planifiées sur Jitsi ou Zoom.

## Définition des objets, de leurs propriétés et de leurs contraintes

Nous allons dans cette section définir les différents objets de notre base de données ainsi que leurs propriétés.

### Le patient

Le patient est l’animal que prend en charge la clinique. C’est lui qui sera soigné et ausculté par le personnel de la clinique vétérinaire. Le patient est caractérisé par :

-   son *espèce*
    
-   son *nom*
    
-   sa *date de naissance* (optionnel)
    
-   son *numéro de puce* (optionnel)
    
-   son *numéro de passeport* (optionnel)
    

Un patient est possédé (ou a été possédé) par un ou plusieurs clients. De plus, un patient est suivi (ou a été suivi) par un ou plusieurs vétérinaires.

### L’espèce

Un patient est caractérisé par son espèce, c’est-à-dire 

> " une population ou un ensemble de populations dont les individus peuvent se reproduire entre eux et engendrer une descendance viable et féconde, dans des conditions naturelles  (Ernst Mayr, 1942). "

L’espèce est caractérisée par :

-   son *nom*
    
-   sa *catégorie*, c’est-à-dire la famille à laquelle elle appartient parmi cette liste : félin, canidé, reptile, rongeur, oiseau ou autre
    
-   sa *taille*, petite ou moyenne, par rapport à la catégorie à laquelle le patient appartient

Un patient ne peut appartenir qu'à une seule espèce. En revanche, il peut y avoir plusieurs patients de la même espèce.


### Le client

Un client de la clinique est une personne possédant un animal de compagnie qui est un patient de cette clinique. Il est caractérisé par :

-   son *nom*
    
-   son *prénom*
    
-   sa *date de naissance*
    
-   son *adresse*
    
-   son *numéro de téléphone*
    

Un client peut être le propriétaire d’un ou plusieurs patients de la clinique, sur une période de temps finie ou en cours. Toutefois, il ne peut être un membre du personnel de celle-ci.


## Les assistants et les vétérinaires

Les assistants et les vétérinaires de la clinique s’occupent des patients lors de consultations. Ils se caractérisent par :

-   un *nom*
    
-   un *prénom*
    
-   une *date de naissance*
    
-   une *adresse*
    
-   un *numéro de téléphone*
    
-   une *spécialité*
    

Contrairement aux vétérinaires, les assistant(e)s ne sont pas autorisé(e)s à prescrire un traitement.

## Le dossier médical

Le dossier médical est propre à chaque patient de la clinique vétérinaire. Il permet de rassembler toutes les entrées réalisées par le personnel de la clinique et d’avoir une vue d’ensemble sur le cas d’un patient.

## La taille

La taille du client est une donnée caractérisée par :

-   une *mesure* (optionnelle) exprimée en mètres
    
-   une *saisie (date et heure)* dans la base de données
    

## Le poids

La poids du client est une donnée caractérisée par :

-   une *mesure* (optionnelle) exprimée en kilogrammes
    
-   une *saisie (date et heure)* dans la base de données
    

  

## La consultation

Chaque patient peut assister à une ou plusieurs consultations. Celles-ci se caractérisent par les propriétés suivantes :

-   une *date de consultation*
    
-   une *observation*
    
-   un(e) membre du *personnel* effectuant la consultation
    
-   la *saisie (date et heure)* de la consultation dans la base de données
    

## Le traitement

Dans le cadre de son suivi, un patient peut se voir administrer un ou plusieurs traitements. Ce traitement est caractérisé par :

-   sa *date de début*
    
-   sa *durée*
    
-   sa *saisie (date et heure)* dans la base de données
    

Un traitement ne peut être prescrit que par un vétérinaire de la clinique et comprend au minimum un médicament.

## L’analyse

Un patient de la clinique peut être sujet à une ou plusieurs analyses. Elle se caractérise par :

-   son *résultat*, un lien vers un document électronique, qui est unique
    
-   sa *saisie (date et heure)* dans la base de données
    

Un patient peut ne pas avoir eu d’analyses pendant son suivi.

## La procédure

La procédure doit être réalisée sur le patient avec sa description. Elle se caractérise par :

  

-   son *nom*
    
-  sa *description*
    
-  sa *saisie (date et heure)* dans la base de données
    

  

## Le médicament

Le médicament est le composé pharmaceutique qui sera administré au patient en fonction de ses besoins. Certains médicaments ne peuvent être prescrits qu’à certaines espèces. Chaque médicament se caractérise par :

-   un *nom de molécule* permettant d’identifier le médicament.
    
-   un ensemble *d’effets*, présentés sous la forme d’une description.
    

## La posologie

La posologie désigne la quantité d'un médicament précis à administrer à un patient donné. Elle est caractérisée par :

-   la *quantité par jour* prescrite pour le médicament à consommer.
    

  
## Les utilisateurs de l'application

  

### L'administrateur de la clinique

Il pourra gérer les patients (animaux), ses clients, son personnel soignant ainsi que les médicaments administrés. Pour cela, il pourra ajouter et mettre à jour la base de données, et les accès aux informations de celle-ci. 

Ainsi, il pourra obtenir des rapports d'activité et des informations statistiques, comme les quantités de médicaments consommées, le nombre de traitements ou de procédures effectuées dans la clinique, ou encore des statistiques sur les espèces d'animaux traitées.

  

### Le personnel

Les membres du personnel peuvent ajouter des données aux objets suivants : taille, poids, consultation, traitement, analyse, procédure et posologie.

Ils pourront également obtenir des informations sur le dossier médical du ou des patients qu’ils suivent.