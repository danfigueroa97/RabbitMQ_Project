import pika
import time

# Conectar a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Asegúrate de declarar la cola
channel.queue_declare(queue='queue2')

# Número máximo de mensajes que se enviarán
max_messages = 10

for i in range(max_messages):
    message = f"Mensaje {i+1}"
    channel.basic_publish(exchange='',
                          routing_key='queue2',  # Esta es la cola a la que el suscriptor escucha
                          body=message)
    print(f"Enviado: Buenas Tardes")
    time.sleep(1)  # Espera de 1 segundo entre mensajes

# Cerrar la conexión al finalizar
connection.close()
print("Publicador terminado.")