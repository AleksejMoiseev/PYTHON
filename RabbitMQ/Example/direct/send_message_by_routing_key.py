import amqp


with amqp.Connection('127.0.0.1:5672', 'user', 'password') as connection:
    channel = connection.channel()
    # gj
    for i in range(10):
        channel.basic_publish(amqp.Message(f"Hello Word {i}"), exchange='amq.direct', routing_key="first")
