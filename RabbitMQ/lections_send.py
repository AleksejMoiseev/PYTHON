import amqp

for i in range(1):

    with amqp.Connection('127.0.0.1:5672', 'user', 'password') as c:
        ch = c.channel()
        ch.basic_publish(amqp.Message("Hello Word"), exchange='amq.direct', routing_key="first")
