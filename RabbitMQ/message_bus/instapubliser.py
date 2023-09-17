from kombu import Connection
from typing import Optional
from message_bus.shema import BrokerScheme
from message_bus.message import Message
from message_bus.interfaces import Publisher


class KombuPublisher(Publisher):

    def __init__(self, scheme: BrokerScheme, rabbit_url: str):
        self._connection: Optional[Connection] = None
        self._scheme = scheme
        self._rabbit_url = rabbit_url

    def __enter__(self):
        self._connection = Connection(self._rabbit_url)
        return self

    def __exit__(self, *exsc):
        self._connection.release()

    @property
    def _producer(self):
        return self._connection.Producer(serializer='json')

    def publish(self, message: Message):
        self._producer.publish(
            message.event.dict(),
            routing_key=message.routing_key,
            declare=self._scheme.queues(),
            exchange=self._scheme.exchange(routing_key=message.routing_key)
        )