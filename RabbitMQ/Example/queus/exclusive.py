import amqp
from time import sleep

with amqp.Connection('127.0.0.1:5672', 'user', 'password') as connection:
    channel = connection.channel()
    channel.queue_declare(queue='exclusive_1', exclusive=True)
    channel.queue_bind(exchange='amq.direct', queue='exclusive_1', routing_key='exclusive_1')
    channel.basic_publish(amqp.Message("Hello Word"), exchange='amq.direct', routing_key="exclusive_1")

    # Для демонстрации, того, что очередь живет пока есть потребители
    # while True:
    #     sleep(1)

    # Читаем сообщения пока открыт канал, очередь автоматически удалится если канал будет закрыт
    def on_message(message):
        print("Received message(delivery tag{}): {}".format(message.delivery_tag, message.body))
        # Сообщаем брокеру, что сообщение получено и его можно удалить
        channel.basic_ack(message.delivery_tag)


    # Передаем потребителю очередь сообщений и обработчик сообщения
    channel.basic_consume(queue='exclusive_1', callback=on_message)
    while True:
        connection.drain_events()
