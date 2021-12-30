import mysql.connector
import os, time

def create_database(db_connection,db_name,cursor):
	cursor.execute(f"CREATE DATABASE {db_name};")
	cursor.execute(f"COMMIT;")
	cursor.execute(f"USE {db_name};")
	
	# Tabla news
	cursor.execute('''CREATE TABLE links(
		id_gifs INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
		linkgif VARCHAR(200)
		);''')

	cursor.execute("SET GLOBAL time_zone = 'UTC';")
	cursor.execute("SET SESSION time_zone = 'UTC';")

	cursor.execute("COMMIT;") 

def insert_data(cursor):
    print("insert")
    cursor.execute('''INSERT INTO links (linkgif) VALUES
    ('https://c.tenor.com/NpnXNhWqKcwAAAAC/metroid-samus-aran.gif'),
	('https://c.tenor.com/QKQab0rXHLwAAAAC/samus-ridley.gif'),
	('https://64.media.tumblr.com/925f4235dd04fd4b0243311b7864ee17/tumblr_phz7nrP0lb1x2utmko1_540.gif'),
	('https://c.tenor.com/ow42W99p1UcAAAAC/metroid-nintendo.gif'),
	('https://64.media.tumblr.com/acc7dee6f18fae6f039168b992830ec2/tumblr_pd7t1agiqW1vdw6kxo1_r2_540.gif'),
	('https://c.tenor.com/H9P9FJXBP1gAAAAd/fortnite-default.gif'),
	('https://64.media.tumblr.com/54771edff4a6af20bafbe87b13474f7d/tumblr_inline_pa7zsfOOiW1qbjpiv_500.gif'),
	('https://64.media.tumblr.com/fd0fd06c5c958a4781bb068d48a6fe07/tumblr_inline_pa7zrlF2G61qbjpiv_1280.gif');
    ''')
    cursor.execute("COMMIT;")

#######################

def main():
	print("start creating database...")

	DATABASE = "bot"

	DATABASE_IP = str(os.environ['DATABASE_IP'])

	DATABASE_USER = "root"
	DATABASE_USER_PASSWORD = "root"
	DATABASE_PORT=3306

	not_connected = True

	while(not_connected):
		try:
			print(DATABASE_IP,"IP")
			db_connection = mysql.connector.connect(user=DATABASE_USER,host=DATABASE_IP,port=DATABASE_PORT, password=DATABASE_USER_PASSWORD)
			not_connected = False

		except Exception as e:
			time.sleep(3)
			print(e, "error!!!")
			print("can't connect to mysql server, might be intializing")
			
	cursor = db_connection.cursor()

	try:
		cursor.execute(f"USE {DATABASE}")
		print(f"Database: {DATABASE} already exists")
	except Exception as e:
		create_database(db_connection,DATABASE,cursor)
		insert_data(cursor)
		print(f"Succesfully created: {DATABASE}")
