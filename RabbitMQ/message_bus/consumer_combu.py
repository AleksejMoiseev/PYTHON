from kombu import Connection, Exchange, Queue
from typing import Callable, Any
from kombu import Consumer
from functools import partial
from message_bus.handler import MessageHandler

media_exchange = Exchange('media', 'direct', durable=True)
video_queue = Queue('video', exchange=media_exchange, routing_key='video')


def process_media(body):
    print(body)


def on_message(body, message, handler):
    handler.handle(body, message)



#
# with Connection('amqp://user:password@localhost//') as connection:
#     with connection.Consumer([video_queue],
#                              callbacks=[process_media]) as consumer:
#         while True:
#             connection.drain_events()

handler = MessageHandler(function=process_media, is_notify_immediately=True)

with Connection('amqp://user:password@localhost//') as conn:
    with conn.channel() as channel:
        consumer = Consumer(channel, video_queue)
        run_message = partial(on_message, handler=handler)
        consumer.register_callback(run_message)

        while True:
            with consumer:
                conn.drain_events()

