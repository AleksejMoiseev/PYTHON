from kombu import Connection, Queue


class BrokerScheme:

    def __init__(self, *queues: Queue):
        self._queues = queues
        self._exchanges = {queue.routing_key: queue.exchange for queue in self._queues}

    def exchange(self, routing_key: str):
        if routing_key in self._exchanges:
            return self._exchanges[routing_key]
        raise Exception()

    def queues(self):
        return [queue for queue in self._queues]

    def declare(self, connection: Connection):
        with connection.channel() as channel:

            for exchange in self._exchanges:
                exchange.declare(channel=channel)

            for queue in self._queues:
                queue.declare(channel=channel)
