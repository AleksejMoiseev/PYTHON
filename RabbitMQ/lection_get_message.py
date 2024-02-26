import amqp

# Создание соединения потребителя
with amqp.Connection(userid='user', password='password') as c:
    ch = c.channel()

    def on_message(message):
        print("Received message(delivery tag{}): {}".format(message.delivery_tag, message.body))
        # Сообщаем брокеру, что сообщение получено и его можно удалить
        ch.basic_ack(message.delivery_tag)

    ch.basic_consume(queue='first', callback=on_message)
    while True:
        c.drain_events()