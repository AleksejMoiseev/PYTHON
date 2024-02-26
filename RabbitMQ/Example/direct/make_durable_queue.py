import amqp

# Создание соединения издателя
# amqp работает поверх TCP/IP
with amqp.Connection('127.0.0.1:5672', 'user', 'password') as connection:
    # Для такого обмена информацией между клиентом и сервером используются каналы.
    # Каналы создаются в рамках определенного подключения. Каждый канал изолирован от других каналов
    # Erlang - процесс
    channel = connection.channel()
    # Создание постоянной очереди  queue='first'
    channel.queue_declare(queue='first', durable=True, auto_delete=False)
    # правило, которое сообщает обменнику в какую из очередей эти сообщения должны попадать
    channel.queue_bind(exchange='amq.direct', queue='first', routing_key='first')

    # отправка сообщения
    channel.basic_publish(amqp.Message("Hello Word"), exchange='amq.direct', routing_key="first")
