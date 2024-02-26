import pika

credentials = pika.PlainCredentials(username='user', password='password')
parameters = pika.ConnectionParameters(host='127.0.0.1', port=5672, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='headers_1', durable=True)
channel.queue_declare(queue='headers_2', durable=True)
# Сообщение попадает по любому из заголовков
channel.queue_bind(exchange='amq.headers', queue='headers_1', arguments={
            'year': 2024,
            'month': 3,
            'x-match': 'any'
        })
# Сообщение попадает по совпадению всех пар ключ: значение
channel.queue_bind(exchange='amq.headers', queue='headers_2', arguments={
            'year': 2024,
            'month': 3,
            'x-match': 'all'
        })

channel.basic_publish(
    exchange='amq.headers',
    body="Topic message A",
    routing_key='',
    properties=pika.BasicProperties(
        headers={
            'year': 2024,
            'month': 3,
        }
    ))