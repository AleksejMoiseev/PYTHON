import amqp

# Создание соединения потребителя
with amqp.Connection(userid='user', password='password') as connection:
    channel = connection.channel()

    def on_message(message):
        print("Received message(delivery tag{}): {}".format(message.delivery_tag, message.body))
        # Сообщаем брокеру, что сообщение получено и его можно удалить
        channel.basic_ack(message.delivery_tag)
    # Передаем потребителю очередь сообщений и обработчик сообщения
    channel.basic_consume(queue='exclusive_1', callback=on_message)
    while True:
        connection.drain_events()