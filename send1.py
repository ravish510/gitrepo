import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.queue_declare(queue='bye')
for i in range(10):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello I am Ravi Shankar!')
for j in range(10):
	channel.basic_publish(exchange='',
                          routing_key='bye',
                          body='Hello I am Ravi Shankar!')
# print(" [x] Sent 'Hello World!'")

connection.close()
