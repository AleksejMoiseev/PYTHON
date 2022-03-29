import pika

credentials = pika.PlainCredentials(username='user', password='password')
parameters = pika.ConnectionParameters(host='127.0.0.1', port=5672, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# cnt = channel.queue_declare(queue='first', passive=True).method.message_count

channel.basic_publish(exchange='amq.fanout', routing_key='', body="Fanout message A")
channel.basic_publish(
    exchange='amq.headers',
    routing_key='head',
    properties=pika.BasicProperties(
        headers={
            'correlation': 1,
        }
    ),
    body="Fanout message A",
)