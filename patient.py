import psycopg2
import datetime


def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'

def afficher_patient(conn):
	i = int(input("Sur quel critere voulez-vous afficher les patients? 1 si vous voulez afficher tous les patients, 2 si vous voulez afficher une espece en particulier, 3 si vous voulez afficher les patients d'un proprietaire"))
	try:
		if i == 1:
   			cur = conn.cursor()
   			sql = "SELECT * FROM Patient"

		elif i == 2:
   		 	_espece = quote(input("Entrez le nom d'espece"))
   		 	cur = conn.cursor()
   		 	sql = "SELECT * FROM Patient WHERE espece = %s" % (_espece)


		elif i == 3:
   		 	_proprietaire = quote(input("Entrez le nom d'un proprietaire"))
   		 	cur = conn.cursor()
   		 	sql = "SELECT * FROM Patient WHERE proprietaire = %s" % (_proprietaire)

		cur.execute(sql)
		
	except psycopg2.IntegrityError as e :
			print("Message systeme :", e)

	res = cur.fetchall()
	i = 0
	while res :
    		print(res[i])
    		i +=1
