CREATE TABLE Client (
	Idc INTEGER PRIMARY KEY,
	nom VARCHAR NOT NULL,
	prenom VARCHAR NOT NULL,
    date_de_naissance DATE NOT NULL,
    adresse VARCHAR NOT NULL,
    num_tel INTEGER NOT NULL,
    CHECK (num_tel BETWEEN 0000000000 AND 9999999999)
);

CREATE TYPE famille AS ENUM ('félin','canidé','reptile', 'rongeur', 'oiseau','autre');
CREATE TYPE hauteur AS ENUM ('petite', 'moyenne');

CREATE TABLE Espece (
	categorie famille UNIQUE NOT NULL, 
	taille hauteur UNIQUE NOT NULL, 
	PRIMARY KEY(categorie, taille)
);


CREATE TABLE Dossier_medical(
	Id INTEGER PRIMARY KEY
);


CREATE TABLE Patient (
	Idp INTEGER ,
	nom VARCHAR,
	date_naissance VARCHAR,
	num_puce INTEGER, 
	num_passeport VARCHAR, 
	espece famille,
	proprietaire INTEGER,
	dossier_medical INTEGER,
	PRIMARY KEY(Idp),
	FOREIGN KEY (espece) REFERENCES Espece(categorie),
	FOREIGN KEY (proprietaire) REFERENCES Client(Idc),
	FOREIGN KEY (dossier_medical) REFERENCES Dossier_medical(Id),
	CHECK ((date_naissance LIKE '[0-9]{4}') OR (date_naissance LIKE '[0-9]{2}/[0-9]{2}/[0-9]{4}') OR (date_naissance LIKE 'inconnue'))
);



CREATE TABLE Veterinaire (
	IdV INTEGER PRIMARY KEY,
	specialite famille, 
	nom VARCHAR UNIQUE NOT NULL,
	prenom VARCHAR UNIQUE NOT NULL, 
	date_de_naissance DATE UNIQUE NOT NULL, 
	adresse VARCHAR UNIQUE NOT NULL, 
	num_telephone INTEGER, 
	FOREIGN KEY (specialite) REFERENCES Espece(categorie),
    CHECK (num_telephone BETWEEN 0000000000 AND 9999999999)

);


CREATE TABLE Traitement (
	IdT INTEGER PRIMARY KEY, 
	date_debut DATE NOT NULL, 
	duree INTEGER NOT NULL, 
	date_heure_saisie DATE, 
	prescrit_par INTEGER, 
	dossier INTEGER,
	FOREIGN KEY (prescrit_par) REFERENCES Veterinaire(IdV),
	FOREIGN KEY (dossier) REFERENCES Dossier_medical(Id)

);


CREATE TABLE Assistant(
	IdA INTEGER PRIMARY KEY, 
	specialite famille, 
	nom VARCHAR NOT NULL, 
	prenom VARCHAR NOT NULL, 
	date_de_naissance DATE NOT NULL, 
	adresse VARCHAR NOT NULL, 
	num_telephone INTEGER,
	FOREIGN KEY (specialite) REFERENCES Espece(categorie),
    CHECK (num_telephone BETWEEN 0000000000 AND 9999999999)
);



CREATE TABLE Suivi_proprietaire (
	client INTEGER, 
	patient INTEGER, 
	date_debut DATE NOT NULL, 
	date_fin DATE, 
	FOREIGN KEY (client) REFERENCES Client(IdC), 
	FOREIGN KEY (patient) REFERENCES Patient(IdP)

);

CREATE TABLE Suivi_veterinaire (
	patient INTEGER, 
	veterinaire INTEGER, 
	date_debut DATE NOT NULL, 
	date_fin DATE NOT NULL, 
	FOREIGN KEY (patient) REFERENCES Patient(IdP),
	FOREIGN KEY (veterinaire) REFERENCES Veterinaire(IdV)

);

CREATE TABLE Consultation (
	date DATE, 
	observation VARCHAR, 
	personnel INTEGER, 
	date_heure_saisie TIMESTAMP, 
	veto_consult INTEGER, 
	dossier INTEGER, 
	PRIMARY KEY (date, date_heure_saisie) , 
	FOREIGN KEY (personnel) REFERENCES Veterinaire(IdV),
	FOREIGN KEY (veto_consult) REFERENCES Veterinaire(IdV), 
	FOREIGN KEY (dossier) REFERENCES Dossier_medical(Id)
 
);



CREATE TABLE Taille (
	mesure NUMERIC(3,1), 
	date_heure_saisie TIMESTAMP, 
	dossier_medical INTEGER REFERENCES Dossier_medical(Id), 
	PRIMARY KEY (mesure, date_heure_saisie) , 
	CHECK (mesure > -1)
);



CREATE TABLE Poids (
    mesure NUMERIC(3,1),
    date_heure_saisie date NOT NULL,
    dossier_medical  INTEGER REFERENCES Dossier_medical(Id),
	CHECK (mesure > -1)
); 

CREATE TABLE Analyses(
  resultat VARCHAR PRIMARY KEY,
  date_heure_saisie TIMESTAMP,
  dossier_medical INTEGER REFERENCES Dossier_medical(Id),
  CHECK (SUBSTR(resultat,1,8) ='https://')
);

CREATE TABLE Medicament (
	nom_molecule VARCHAR PRIMARY KEY, 
	effets VARCHAR NOT NULL
);

CREATE TABLE Est_compatible(
	medicament VARCHAR NOT NULL, 
	espece famille NOT NULL,
	FOREIGN KEY (medicament) REFERENCES Medicament(nom_molecule), 
	FOREIGN KEY (espece) REFERENCES Espece(categorie)
); 

CREATE TABLE Posologie (
	traitement INTEGER, 
	medicament VARCHAR NOT NULL, 
	quantite_par_jour INTEGER, 
	FOREIGN KEY (traitement) REFERENCES Traitement(IdT), 
	FOREIGN KEY (medicament) REFERENCES Medicament(nom_molecule), 
	CHECK (quantite_par_jour > 0)
);

CREATE TABLE Procedure (
	nom VARCHAR NOT NULL, 
	description VARCHAR NOT NULL,
	date_heure_saisie TIMESTAMP NOT NULL, 
	assistant INTEGER UNIQUE, 
	veterinaire INTEGER UNIQUE, 
	dossier INTEGER, 
    PRIMARY KEY (nom, dossier, date_heure_saisie) ,
	FOREIGN KEY (assistant) REFERENCES Assistant(IdA), 
	FOREIGN KEY (veterinaire) REFERENCES Veterinaire(IdV), 
    CHECK (((assistant IS NULL) AND (veterinaire IS NOT NULL)) OR ((assistant IS NOT NULL) AND (veterinaire IS NULL))) 
);


CREATE TABLE Speveto (
	veterinaire INTEGER, 
	espece famille NOT NULL, 
	FOREIGN KEY (veterinaire) REFERENCES Veterinaire(IdV), 
	FOREIGN KEY (espece) REFERENCES Espece(categorie)
);


CREATE TABLE Speassis (
	assistant INTEGER,
    espece famille NOT NULL, 
    FOREIGN KEY (assistant) REFERENCES Assistant(IdA), 
    FOREIGN KEY (espece) REFERENCES Espece(categorie)
);




 

	
	
	
