from typing import Optional, Callable
from functools import partial

from kombu import Connection, Queue, Consumer, Exchange

from message_bus.handler import MessageHandler


class KombuConsumer:

    def __init__(self, rabbit_url: str, queue: Queue, function: Callable, is_notify_immediately: bool):
        self._queue = queue
        self._rabbit_url = rabbit_url
        self._function = function
        self._is_ack = is_notify_immediately

    def _get_handler(self):
        return MessageHandler(function=self._function, is_notify_immediately=self._is_ack)

    def _get_consumer(self, channel):
        consumer = Consumer(channel, self._queue)
        handler = self._get_handler()
        on_message = partial(self.on_message, handler=handler)
        consumer.register_callback(on_message)
        return consumer

    @staticmethod
    def on_message(body, message, handler):
        handler.handle(body, message)

    def consume(self):
        with Connection(self._rabbit_url) as conn:
            with conn.channel() as channel:
                consumer = self._get_consumer(channel=channel)
                while True:
                    with consumer:
                        conn.drain_events()


if __name__ == '__main__':
    media_exchange = Exchange('media', 'direct', durable=True)
    video_queue = Queue('video', exchange=media_exchange, routing_key='video')


    def process_media(body):
        print(body)


    consumer = KombuConsumer(
        rabbit_url='amqp://user:password@localhost//',
        function=process_media,
        queue=video_queue,
        is_notify_immediately=True
    )
    consumer.consume()