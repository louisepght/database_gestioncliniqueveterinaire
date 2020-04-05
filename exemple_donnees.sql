INSERT INTO Client
VALUES ('0698723654', 'Bloy', 'Jeanne', '1970-01-13', 'Rue des Oliviers, nº5, 60200, Compiègne'),
('0667221257', 'Illich', 'Ivan', '1968-02-24', 'Rue de la Résistance, nº12, 60200, Compiègne'),
('0798723654', 'Charbonneau', 'Bernard', '1990-08-30', 'Rue des Veneurs, nº4, 60200, Compiègne');


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
('05');


INSERT INTO Patient (Idp, nom, date_naissance, num_puce, num_passeport, espece, espece_taille, proprietaire, dossier_medical)
VALUES ('01', 'Fifou', 'inconnue',NULL, 'FRAA59790201', 'félin', 'moyenne', '0698723654', '01'),
('02', 'Bulby', 'inconnue','87602100', NULL, 'oiseau','petite', '0667221257', '02'),
('03', 'Fofma', 'inconnue',NULL, NULL, 'reptile','petite', '0798723654', '03');


INSERT INTO Veterinaire (num_telephone, nom, prenom, date_de_naissance, adresse)
VALUES ('0245728090', 'de Montfort', 'Paul-Étienne', '1955-08-29', 'Avenue du Général de Gaulle, nº20, 60200, Compiègne'),
('0245728091', 'Henry', 'Edwiges', '1978-09-19', 'Impasse de la Madeleine, nº20, 60200, Compiègne'),
('0245728092', 'Weil', 'Simone', '1982-03-11', 'Rue Saint-Joseph, nº132, 60200, Compiègne');


INSERT INTO Traitement (IdT, date_debut, duree, date_heure_saisie, prescrit_par, dossier)
VALUES ('01', '2018-05-05', '4', '2018-05-05, 13:00', '0245728090', '01'),
('02', '2019-05-05', '4', '2019-05-06, 15:48', '0245728091', '02'),
('03', '2019-05-15', '8', '2019-06-01, 09:08', '0245728092', '03');

INSERT INTO Assistant (num_telephone, nom, prenom, date_de_naissance, adresse)
VALUES ('0345728090', 'Henry', 'Michel', '1965-08-09', 'Impasse de la Madeleine, nº20, 60200, Compiègne'),
('0345728091', 'Mounier', 'Emmanuel', '1976-12-25', 'Square des églises, nº58, 60200, Compiègne'),
('0345728092', 'Ellul', 'Jacques', '1965-10-05', 'Rue de la Liberté, nº2, 60200, Compiègne');
 

INSERT INTO Suivi_proprietaire (client, patient, date_debut, date_fin)
VALUES ('0698723654', '01', '2012-07-05', '2017-07-04'),
('0667221257', '02', '2020-02-01', '2020-04-01'),
('0798723654', '03', '2018-12-01', '2020-01-01');


INSERT INTO Suivi_veterinaire (patient, veterinaire, date_debut,date_fin)
VALUES ('01', '0245728090', '2012-07-05', '2017-07-04'),
('02', '0245728091', '2020-02-01', '2020-04-01'),
('03', '0245728092', '2018-12-01', '2020-01-01');


INSERT INTO Consultation(date, observation,date_heure_saisie, veterinaire, dossier)
VALUES ('2018-05-01', 'rien à signaler', '2018-05-04, 12:00', '0245728090', '01');


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
VALUES ('Paracétamol','XXX'),
('Chloroquine','YYY'),
('Tymol', 'ZZZ'),
('Pyridine','WWW');

INSERT INTO Est_autorise (medicament, espece, espece_taille)
VALUES ('Paracétamol', 'oiseau','petite'),
('Paracétamol', 'canidé', 'petite'),
('Tymol', 'félin', 'moyenne'),
('Chloroquine', 'reptile','petite');


INSERT INTO Posologie (traitement, medicament, quantite_par_jour)
VALUES ('01', 'Paracétamol', '2'),
('03', 'Tymol', '4'),
('02', 'Chloroquine', '3'),
('02', 'Tymol', '5');

INSERT INTO Procedure (nom, description, date_heure_saisie, assistant, veterinaire, dossier)
VALUES ('Procedure1', 'Blabla', '2018-05-10, 19:00', NULL, '0245728091', '01'),
('Procedure2', 'BliBli', '2020-12-10, 16:42', '0345728092', NULL, '02');


INSERT INTO Speveto (veterinaire, espece, espece_taille)
VALUES ('0245728090', 'canidé', 'petite'),
('0245728091', 'oiseau', 'petite'),
('0245728092', 'félin', 'moyenne');


INSERT INTO Speassis (assistant, espece, espece_taille)
VALUES ('0345728090', 'canidé', 'petite'),
('0345728091', 'oiseau', 'petite'),
('0345728092', 'félin', 'moyenne');
