from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    UNLOCKED = auto()
    FAILED = auto()


class DoorLock:

    def __init__(self, code):
        self.code = code
        self._state = State.LOCKED
        self._entry = ''

    def run(self):

        while True:
            match self._state:
                case State.LOCKED:
                    self._entry = input('Введите код > : ')
                    if self._entry == self.code:
                        self._state = State.UNLOCKED
                    else:
                        self._state = State.FAILED

                case State.FAILED:
                    print('Попытка провалилась')
                    self._entry = ''
                    self._state = State.LOCKED

                case State.UNLOCKED:
                    print('Замок открыт')
                    break


if __name__ == '__main__':
    lock = DoorLock(code='1234')
    lock.run()