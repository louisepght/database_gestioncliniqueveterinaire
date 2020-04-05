INSERT INTO Client
VALUES ('0698723654', 'Bloy', 'Jeanne', '1970-01-13', 'Rue des Oliviers, nº5, 60200, Compiègne'),
('0667221257', 'Illich', 'Ivan', '1968-02-24', 'Rue de la Résistance, nº12, 60200, Compiègne'),
('0787236543', 'Charbonneau', 'Bernard', '1990-08-30', 'Rue des Veneurs, nº4, 60200, Compiègne'),
('0787236520', 'Gunther', 'Anders', '1967-08-30', 'Rue de Lyon, nº5, 60000, Amiens'),
('0787636584', 'Richardo', 'Maelle', '1997-08-09', 'Rue de mai, nº3, 63000, Clermont-ferrand'),
('0798723654', 'Lejeune', 'Mathilde', '1996-06-24', 'Rue Charles de Gaulle, nº4, 60200, Compiègne'),
('0667551457', 'Dupont', 'Clémence', '1988-05-07', 'Rue Winston Churchill, nº6, 60200, Compiègne'),
('0781890675', 'Simondon', 'Gilbert', '1970-08-04', 'Rue Saint-Joseph, nº4, 60200, Compiègne');

INSERT INTO Espece VALUES ('félin', 'petite'),
('canidé', 'petite'),
('oiseau', 'petite'),
('reptile','petite'),
('rongeur','petite'),
('autre','petite'),
('félin', 'moyenne'),
('canidé', 'moyenne'),
('oiseau', 'moyenne'),
('reptile','moyenne'),
('rongeur','moyenne'),
('autre','moyenne');


INSERT INTO Dossier_medical (Id)
VALUES ('01'),
('02'),
('03'),
('04'),
('05'),
('06'),
('07'),
('08'),
('09'),
('10'),
('11'),
('12');


INSERT INTO Patient (Idp, nom, date_naissance, num_puce, num_passeport, espece, espece_taille, proprietaire, dossier_medical)
VALUES ('01', 'Fifou', 'inconnue',NULL, 'FRAA59790201', 'félin', 'moyenne', '0698723654', '01'),
('02', 'Bulby', 'inconnue','87602100', NULL, 'oiseau','petite', '0667221257', '02'),
('04', 'Nemo', 'inconnue','87602130', NULL, 'félin','petite', '0787636584', '04'),
('05', 'Caline', 'inconnue','87302130', '403060897856', 'félin','moyenne', '0787236520', '05'),
('06', 'Ruby', 'inconnue','87562130', '403060577856', 'rongeur','petite', '0667551457', '06'),
('03', 'Fofma', 'inconnue',NULL, NULL, 'reptile','petite', '0798723654', '03');


INSERT INTO Veterinaire (num_telephone, nom, prenom, date_de_naissance, adresse)
VALUES ('0245728090', 'de Montfort', 'Paul-Étienne', '1955-08-29', 'Avenue du Général de Gaulle, nº20, 60200, Compiègne'),
('0245728091', 'Henry', 'Edwiges', '1978-09-19', 'Impasse de la Madeleine, nº20, 60200, Compiègne'),
('0245728089', 'Dupont', 'Clemence', '1970-09-19', 'Boulevard Gambetta, nº2, 60200, Compiègne'),
('0245728051', 'Lejeune', 'Jérôme', '1967-09-19', 'Rue Pierre Crin, nº20, 60200, Compiègne'),
('0245724591', 'May', 'Erica', '1992-12-19', 'Rue Carnot, nº20, 60200, Compiègne'),
('0245728092', 'Weil', 'Simone', '1982-03-11', 'Rue Saint-Joseph, nº132, 60200, Compiègne');


INSERT INTO Traitement (IdT, date_debut, duree, date_heure_saisie, prescrit_par, dossier)
VALUES ('01', '2018-05-05', '4', '2018-05-05, 13:00', '0245728090', '01'),
('02', '2019-05-06', '7', '2019-05-06, 15:48', '0245728091', '02'),
('04', '2019-05-07', '4', '2019-05-04, 16:48', '0245728051', '04'),
('05', '2019-05-08', '2', '2019-05-03, 15:58', '0245728092', '05'),
('06', '2019-05-09', '8', '2019-05-02, 15:49', '0245724591', '06'),
('03', '2019-05-15', '8', '2019-06-01, 09:10', '0245728090', '03');


INSERT INTO Assistant (num_telephone, nom, prenom, date_de_naissance, adresse)
VALUES ('0345728090', 'Henry', 'Michel', '1965-08-09', 'Impasse de la Madeleine, nº20, 60200, Compiègne'),
('0345728091', 'Mounier', 'Emmanuel', '1976-12-25', 'Square des églises, nº58, 60200, Compiègne'),
('0345728092', 'Ellul', 'Jacques', '1965-10-05', 'Rue de la Liberté, nº2, 60200, Compiègne'),
('0345728093', 'Courbet', 'Gustave', '1982-08-09', 'Avenue Napoléon III, nº20, 60200, Compiègne'),
('0345728094', 'Rodrigues', 'Maria', '1969-01-29', 'Rue des Cordeliers, nº46, 60200, Compiègne'),
('0345728095', 'Martin', 'Zélie', '1980-04-08', 'Rue du Port à Bateaux, nº120, 60200, Compiègne');
 

INSERT INTO Suivi_proprietaire (client, patient, date_debut, date_fin)
VALUES ('0698723654', '01', '2012-07-05', '2017-07-04'),
('0667221257', '02', '2020-02-01', '2020-04-01'),
('0798723654', '03', '2018-12-01', '2020-01-01'),
('0787636584', '04','2017-11-21', '2018-11-20'),
('0787236520', '05','2015-06-01', '2019-05-31'),
('0667551457', '06', '2014-05-01', '2018-05-31');

INSERT INTO Suivi_veterinaire (patient, veterinaire, date_debut,date_fin)
VALUES ('01', '0245728090', '2012-07-05', '2017-07-04'),
('02', '0245728091', '2020-02-01', '2020-04-01'),
('03', '0245728092', '2018-12-01', '2020-01-01');


INSERT INTO Consultation(date, observation,date_heure_saisie, veterinaire, dossier)
VALUES ('2018-05-01', 'rien à signaler', '2018-05-04, 12:00', '0245728090', '01'), 
('2018-05-02', 'fracture de la patte', '2018-05-04, 12:09', '0245728092', '03'),
('2018-05-03', 'hernie', '2018-05-04, 12:30', '0245728091', '05');


INSERT INTO Taille (numero, mesure, date_heure_saisie, dossier_medical)
VALUES ('01', '80.3', '2018-05-05 18:00', '01'),
('02', '11.8', '2019-05-08 19:32', '02');


INSERT INTO Poids (numero, mesure, date_heure_saisie, dossier_medical)
VALUES ('01', '90.5', '2018-05-05, 18:05', '01'), 
('02', '62.7', '2019-05-06, 19:33', '02');


INSERT INTO Analyses (resultat, date_heure_saisie, dossier_medical)
VALUES('https://veto-result1.org', '2018-06-10, 19:00', '01'),
('https://veto-result2.org','2019-10-23, 08:37','02'),
('https://veto-result3.org', '2017-05-19, 15:30', '03');


INSERT INTO Medicament (nom_molecule, effets)
VALUES ('Paracétamol','fluidifie le sang'),
('Chloroquine','stimule les battements cardiaques'),
('Ibuprofène','calme les douleurs'),
('Anti-puce','purifie les muqueuses'),
('Tymol', 'facilite le transit'),
('Pyridine','augmente les anticorps');

INSERT INTO Est_autorise (medicament, espece, espece_taille)
VALUES ('Paracétamol', 'oiseau','petite'),
('Paracétamol', 'canidé', 'petite'),
('Tymol', 'félin', 'moyenne'),
('Ibuprofène', 'félin', 'petite'),
('Anti-puce', 'canidé', 'moyenne'),
('Chloroquine', 'reptile','petite');


INSERT INTO Posologie (traitement, medicament, quantite_par_jour)
VALUES ('01', 'Paracétamol', '2'),
('03', 'Tymol', '4'),
('02', 'Chloroquine', '3'),
('04', 'Ibuprofène', '2'),
('05', 'Anti-puce', '1'),
('06', 'Tymol', '5');


INSERT INTO Procedure (nom, description, date_heure_saisie, assistant, veterinaire, dossier)
VALUES ('Procedure1', 'ablation d’un oeil', '2018-05-10, 19:00', NULL, '0245728091', '01'),
('Procedure2', 'anesthésie totale', '2020-12-10, 16:42', '0345728093', NULL, '02'),
('Procedure3', 'pansement', '2020-09-10, 16:30', '0345728095',NULL, '07'),
('Procedure4', 'chirurgie de la patte', '2019-12-10, 14:42', '0345728092', NULL, '09');


INSERT INTO Speveto (veterinaire, espece, espece_taille)
VALUES ('0245728090', 'félin','petite'),
('0245728091', 'canidé','moyenne'),
('0245728089', 'félin','moyenne'),
('0245728091', 'rongeur','moyenne'),
('0245724591', 'oiseau','petite'),
('0245728092', 'reptile','petite');


INSERT INTO Speassis (assistant, espece, espece_taille)
VALUES 
('0345728090','oiseau','petite'),
('0345728091', 'félin','moyenne'),
('0345728092', 'félin','petite'),
('0345728093', 'rongeur','petite'),
('0345728094', 'canidé','moyenne'),
('0345728095', 'canidé','petite');



