import pika
import time

# Conectar a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Asegúrate de declarar la cola
channel.queue_declare(queue='queue1')

# Número máximo de mensajes que se enviarán
max_messages = 10

for i in range(max_messages):
    message = f"Mensaje {i+1}"
    channel.basic_publish(exchange='',
                          routing_key='queue1',  # Esta es la cola a la que el suscriptor escucha
                          body=message)
    print(f"Enviado: Buenos Dias")
    time.sleep(1)  # Espera de 1 segundo entre mensajes

# Cerrar la conexión al finalizar
connection.close()
print("Publicador terminado.")