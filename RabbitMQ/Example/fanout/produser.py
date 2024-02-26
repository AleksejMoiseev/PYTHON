import pika

credentials = pika.PlainCredentials(username='user', password='password')
parameters = pika.ConnectionParameters(host='127.0.0.1', port=5672, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='fanout_1', durable=True)
channel.queue_declare(queue='fanout_2', durable=True)

channel.queue_bind(exchange='amq.fanout', queue='fanout_1')
channel.queue_bind(exchange='amq.fanout', queue='fanout_2')


channel.basic_publish(exchange='amq.fanout', body="Topic message A", routing_key='')