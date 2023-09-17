from abc import ABC, abstractmethod
from message_bus.message import Message


class Publisher(ABC):
    @abstractmethod
    def publish(self, message: Message):
        pass