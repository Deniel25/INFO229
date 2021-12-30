import mysql.connector
import os, time
import pika
import create_database


print("start links manager...")
create_database.main()

DATABASE = "bot"

DATABASE_IP = str(os.environ['DATABASE_IP'])

DATABASE_USER = "root"
DATABASE_USER_PASSWORD = "root"
DATABASE_PORT=3306

time.sleep(10)

########### CONNEXIÓN A RABBIT MQ #######################

HOST = os.environ['RABBITMQ_HOST']
print("rabbit:"+HOST)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'cartero'
channel.exchange_declare(exchange='cartero', exchange_type='topic', durable=True)

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue="links", exclusive=True, durable=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='cartero', queue=queue_name, routing_key="links")


##########################################################


########## ESPERA Y HACE ALGO CUANDO RECIBE UN MENSAJE ####

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
	print(body.decode("UTF-8"))
	arguments = body.decode("UTF-8").split(" ")

	if (arguments[0]==">baby" or arguments[0]==">gif01"):
		db_connection = mysql.connector.connect(user=DATABASE_USER,host=DATABASE_IP,port=DATABASE_PORT, password=DATABASE_USER_PASSWORD)
		cursor = db_connection.cursor()
		cursor.execute(f"USE {DATABASE}")
		cursor.execute(f'''SELECT linkgif FROM links WHERE id_gifs=1;''')
		#print(result)

		for (linksgif) in cursor:
			a= linksgif[0]
			result="{}".format(a)

			########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
			print("send a new message to rabbitmq: "+result)
			channel.basic_publish(exchange='cartero',routing_key="discord_writer",body=result)

	if (arguments[0]==">aproach" or arguments[0]==">gif02"):
		db_connection = mysql.connector.connect(user=DATABASE_USER,host=DATABASE_IP,port=DATABASE_PORT, password=DATABASE_USER_PASSWORD)
		cursor = db_connection.cursor()
		cursor.execute(f"USE {DATABASE}")
		cursor.execute(f'''SELECT linkgif FROM links WHERE id_gifs=2;''')
		#print(result)

		for (linksgif) in cursor:
			a= linksgif[0]
			result="{}".format(a)

			########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
			print("send a new message to rabbitmq: "+result)
			channel.basic_publish(exchange='cartero',routing_key="discord_writer",body=result)

	if (arguments[0]==">metroids" or arguments[0]==">gif03"):
		db_connection = mysql.connector.connect(user=DATABASE_USER,host=DATABASE_IP,port=DATABASE_PORT, password=DATABASE_USER_PASSWORD)
		cursor = db_connection.cursor()
		cursor.execute(f"USE {DATABASE}")
		cursor.execute(f'''SELECT linkgif FROM links WHERE id_gifs=3;''')
		#print(result)

		for (linksgif) in cursor:
			a= linksgif[0]
			result="{}".format(a)

			########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
			print("send a new message to rabbitmq: "+result)
			channel.basic_publish(exchange='cartero',routing_key="discord_writer",body=result)
  
	if (arguments[0]==">like" or arguments[0]==">gif04"):
		db_connection = mysql.connector.connect(user=DATABASE_USER,host=DATABASE_IP,port=DATABASE_PORT, password=DATABASE_USER_PASSWORD)
		cursor = db_connection.cursor()
		cursor.execute(f"USE {DATABASE}")
		cursor.execute(f'''SELECT linkgif FROM links WHERE id_gifs=4;''')
		#print(result)

		for (linksgif) in cursor:
			a= linksgif[0]
			result="{}".format(a)

			########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
			print("send a new message to rabbitmq: "+result)
			channel.basic_publish(exchange='cartero',routing_key="discord_writer",body=result)

	if (arguments[0]==">guayando" or arguments[0]==">gif05"):
		db_connection = mysql.connector.connect(user=DATABASE_USER,host=DATABASE_IP,port=DATABASE_PORT, password=DATABASE_USER_PASSWORD)
		cursor = db_connection.cursor()
		cursor.execute(f"USE {DATABASE}")
		cursor.execute(f'''SELECT linkgif FROM links WHERE id_gifs=5;''')
		#print(result)

		for (linksgif) in cursor:
			a= linksgif[0]
			result="{}".format(a)

			########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
			print("send a new message to rabbitmq: "+result)
			channel.basic_publish(exchange='cartero',routing_key="discord_writer",body=result)

	if (arguments[0]==">fornite" or arguments[0]==">gif06"):
		db_connection = mysql.connector.connect(user=DATABASE_USER,host=DATABASE_IP,port=DATABASE_PORT, password=DATABASE_USER_PASSWORD)
		cursor = db_connection.cursor()
		cursor.execute(f"USE {DATABASE}")
		cursor.execute(f'''SELECT linkgif FROM links WHERE id_gifs=6;''')
		#print(result)

		for (linksgif) in cursor:
			a= linksgif[0]
			result="{}".format(a)

			########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
			print("send a new message to rabbitmq: "+result)
			channel.basic_publish(exchange='cartero',routing_key="discord_writer",body=result)

	if (arguments[0]==">ridley" or arguments[0]==">gif07"):
		db_connection = mysql.connector.connect(user=DATABASE_USER,host=DATABASE_IP,port=DATABASE_PORT, password=DATABASE_USER_PASSWORD)
		cursor = db_connection.cursor()
		cursor.execute(f"USE {DATABASE}")
		cursor.execute(f'''SELECT linkgif FROM links WHERE id_gifs=7;''')
		#print(result)

		for (linksgif) in cursor:
			a= linksgif[0]
			result="{}".format(a)

			########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
			print("send a new message to rabbitmq: "+result)
			channel.basic_publish(exchange='cartero',routing_key="discord_writer",body=result)

	if (arguments[0]==">cannon" or arguments[0]==">gif08"):
		db_connection = mysql.connector.connect(user=DATABASE_USER,host=DATABASE_IP,port=DATABASE_PORT, password=DATABASE_USER_PASSWORD)
		cursor = db_connection.cursor()
		cursor.execute(f"USE {DATABASE}")
		cursor.execute(f'''SELECT linkgif FROM links WHERE id_gifs=8;''')
		#print(result)
		
		for (linksgif) in cursor:
			a= linksgif[0]
			result="{}".format(a)

			########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
			print("send a new message to rabbitmq: "+result)
			channel.basic_publish(exchange='cartero',routing_key="discord_writer",body=result)




channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()



#######################