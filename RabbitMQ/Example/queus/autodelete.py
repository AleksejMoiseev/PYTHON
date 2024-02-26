import amqp

with amqp.Connection('127.0.0.1:5672', 'user', 'password') as connection:
    with connection.channel() as channel:
        channel.queue_declare(queue='autodelete', auto_delete=True)
        channel.queue_bind(exchange='amq.direct', queue='autodelete', routing_key='autodelete')
        channel.basic_publish(amqp.Message("Hello Word"), exchange='amq.direct', routing_key="autodelete")
