CREATE TABLE Client (
    num_tel VARCHAR(10),
    nom VARCHAR NOT NULL,
    prenom VARCHAR NOT NULL,
    date_de_naissance DATE NOT NULL,
    adresse VARCHAR NOT NULL,
    PRIMARY KEY (num_tel),
    UNIQUE (nom, prenom, date_de_naissance,adresse),
    CHECK (LENGTH(num_tel)=10)
);

CREATE TABLE Espece (
    categorie VARCHAR NOT NULL, 
    taille VARCHAR NOT NULL,
    CHECK (categorie IN ('félin','canidé','reptile', 'rongeur', 'oiseau','autre')),
    CHECK (taille IN ('petite', 'moyenne')),
    PRIMARY KEY(categorie, taille)
);

CREATE TABLE Dossier_medical(
    Id INTEGER PRIMARY KEY
);

CREATE TABLE Patient (
    Idp INTEGER,
    nom VARCHAR NOT NULL,
    date_naissance VARCHAR,
    num_puce VARCHAR(8), 
    num_passeport VARCHAR(12), 
    espece VARCHAR NOT NULL,
    espece_taille VARCHAR NOT NULL,
    proprietaire VARCHAR,
    dossier_medical INTEGER,
    PRIMARY KEY(Idp),
    FOREIGN KEY (espece,espece_taille) REFERENCES Espece(categorie,taille), 
    FOREIGN KEY (proprietaire) REFERENCES Client(num_tel),
    FOREIGN KEY (dossier_medical) REFERENCES Dossier_medical(Id),
    CHECK ((LENGTH(date_naissance)=4) OR (LENGTH(date_naissance)=10) OR (date_naissance LIKE 'inconnue')),
    CHECK (LENGTH(num_puce)= 8),
    CHECK (LENGTH(num_passeport)= 12)
);


CREATE TABLE Veterinaire (
    num_telephone VARCHAR(10),
    nom VARCHAR NOT NULL,
    prenom VARCHAR NOT NULL, 
    date_de_naissance DATE NOT NULL, 
    adresse VARCHAR UNIQUE NOT NULL,
    PRIMARY KEY (num_telephone),
    UNIQUE (nom, prenom, date_de_naissance,adresse),
    CHECK (LENGTH(num_telephone)=10)
);

CREATE TABLE Traitement (
    IdT INTEGER PRIMARY KEY, 
    date_debut DATE NOT NULL, 
    duree INTEGER NOT NULL, 
    date_heure_saisie TIMESTAMP, 
    prescrit_par VARCHAR NOT NULL, 
    dossier INTEGER,
    PRIMARY KEY (IdT),
    FOREIGN KEY (prescrit_par) REFERENCES Veterinaire(num_telephone),
    FOREIGN KEY (dossier) REFERENCES Dossier_medical(Id)
);

CREATE TABLE Assistant(
    num_telephone VARCHAR(10), 
    nom VARCHAR NOT NULL, 
    prenom VARCHAR NOT NULL, 
    date_de_naissance DATE NOT NULL, 
    adresse VARCHAR NOT NULL, 
    PRIMARY KEY (num_telephone),
    UNIQUE (nom, prenom, date_de_naissance,adresse),
    CHECK (LENGTH(num_telephone)=10)
);

CREATE TABLE Suivi_proprietaire (
    client VARCHAR(10), 
    patient INTEGER, 
    date_debut DATE NOT NULL, 
    date_fin DATE,
    PRIMARY KEY (client, patient), 
    FOREIGN KEY (client) REFERENCES Client(num_tel), 
    FOREIGN KEY (patient) REFERENCES Patient(IdP)

);

CREATE TABLE Suivi_veterinaire (
    patient INTEGER, 
    veterinaire VARCHAR(10), 
    date_debut DATE NOT NULL, 
    date_fin DATE NOT NULL,
    PRIMARY KEY (patient, veterinaire), 
    FOREIGN KEY (patient) REFERENCES Patient(IdP),
    FOREIGN KEY (veterinaire) REFERENCES Veterinaire(num_telephone)
);

CREATE TABLE Consultation (
    date DATE, 
    observation VARCHAR NOT NULL, 
    date_heure_saisie TIMESTAMP, 
    veterinaire VARCHAR NOT NULL, 
    dossier INTEGER, 
    PRIMARY KEY (date, dossier), 
    FOREIGN KEY (veterinaire) REFERENCES Veterinaire(num_telephone), 
    FOREIGN KEY (dossier) REFERENCES Dossier_medical(Id)
);

CREATE TABLE Taille (
    numero INTEGER,
    mesure NUMERIC(3,1)NOT NULL, 
    date_heure_saisie TIMESTAMP NOT NULL, 
    dossier_medical INTEGER REFERENCES Dossier_medical(Id), 
    PRIMARY KEY (numero), 
    CHECK  (mesure >= 0)
);

CREATE TABLE Poids (
    numero INTEGER,
    mesure NUMERIC(3,1) NOT NULL,
    date_heure_saisie date NOT NULL,
    dossier_medical INTEGER REFERENCES Dossier_medical(Id),
    PRIMARY KEY (numero),
    CHECK (mesure >= 0)
); 

CREATE TABLE Analyses (
    resultat VARCHAR PRIMARY KEY NOT NULL,
    date_heure_saisie TIMESTAMP,
    dossier_medical INTEGER REFERENCES Dossier_medical(Id),
    CHECK (SUBSTR(resultat,1,8) ='https://')

);

CREATE TABLE Medicament (
    nom_molecule VARCHAR PRIMARY KEY, 
    effets VARCHAR NOT NULL
);

CREATE TABLE Est_autorise(
    medicament VARCHAR, 
    espece VARCHAR,
    espece_taille VARCHAR,
    PRIMARY KEY (medicament, espece, espece_taille),
    FOREIGN KEY (medicament) REFERENCES Medicament(nom_molecule), 
    FOREIGN KEY (espece, espece_taille) REFERENCES Espece(categorie,taille)
); 

CREATE TABLE Posologie (
    traitement INTEGER, 
    medicament VARCHAR, 
    quantite_par_jour INTEGER NOT NULL, 
    PRIMARY KEY (traitement, medicament),
    FOREIGN KEY (traitement) REFERENCES Traitement(IdT), 
    FOREIGN KEY (medicament) REFERENCES Medicament(nom_molecule), 
    CHECK (quantite_par_jour > 0)

);

CREATE TABLE Procedure (
    nom VARCHAR, 
    description VARCHAR NOT NULL,
    date_heure_saisie TIMESTAMP, 
    assistant VARCHAR UNIQUE, 
    veterinaire VARCHAR UNIQUE, 
    dossier INTEGER, 
    PRIMARY KEY (nom, dossier, date_heure_saisie) ,
    FOREIGN KEY (assistant) REFERENCES Assistant(num_telephone), 
    FOREIGN KEY (veterinaire) REFERENCES Veterinaire(num_telephone), 
    CHECK (((assistant IS NULL) AND (veterinaire IS NOT NULL)) OR ((assistant IS NOT NULL) AND (veterinaire IS NULL))) 
);

CREATE TABLE Speveto (
    veterinaire VARCHAR, 
    espece VARCHAR, 
    espece_taille VARCHAR, 
    PRIMARY KEY (veterinaire, espece, espece_taille),
    FOREIGN KEY (veterinaire) REFERENCES Veterinaire(num_telephone), 
    FOREIGN KEY (espece, espece_taille) REFERENCES Espece(categorie,taille)
);

CREATE TABLE Speassis (
    assistant VARCHAR,
    espece VARCHAR, 
    espece_taille VARCHAR,
    PRIMARY KEY (assistant, espece, espece_taille),
    FOREIGN KEY (assistant) REFERENCES Assistant(num_telephone), 
    FOREIGN KEY (espece, espece_taille) REFERENCES Espece(categorie,taille)

);

	
