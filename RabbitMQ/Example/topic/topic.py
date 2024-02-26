import pika

credentials = pika.PlainCredentials(username='user', password='password')
parameters = pika.ConnectionParameters(host='127.0.0.1', port=5672, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='second_1', durable=True)
channel.queue_bind(exchange='amq.topic', queue='second_1', routing_key='name.*.height')
channel.queue_declare(queue='second_2', durable=True)
channel.queue_bind(exchange='amq.topic', queue='second_2', routing_key='name.age.*')


#channel.basic_publish(exchange='amq.topic', routing_key='name.no_age.height', body="Topic message name_age_height")
channel.basic_publish(exchange='amq.topic', routing_key='name.age.rrrrr', body="Topic message A")
