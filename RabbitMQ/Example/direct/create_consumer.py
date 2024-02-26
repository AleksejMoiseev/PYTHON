import amqp

# Создание соединения потребителя
with amqp.Connection(userid='user', password='password') as connection:
    channel = connection.channel()
    channel.basic_qos(prefetch_count=5, a_global=False, prefetch_size=0)

    def on_message(message):
        print('!!!!!!!!!!!!!', message.body, message.delivery_tag)
        # print("Received message(delivery tag{}): {}".format(message.delivery_tag, message.body))
        # # Сообщаем брокеру, что сообщение получено и его можно удалить
        # channel.basic_ack(message.delivery_tag)
        channel.basic_reject(message.delivery_tag, requeue=False)
    # Передаем потребителю очередь сообщений и обработчик сообщения
    channel.basic_consume(queue='first', callback=on_message)
    while True:
        connection.drain_events()