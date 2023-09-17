from typing import Callable, Any


class MessageHandler:
    def __init__(self, function: Callable[[Any], Any], is_notify_immediately: bool):
        self._function = function
        self._is_notify_immediately = is_notify_immediately

    def handle(self, body, message):
        if self._is_notify_immediately:
            print('!!!!!!!!!!!!!!!!!')
            message.ack()

        self._function(body)

        if not self._is_notify_immediately:
            message.ack()
