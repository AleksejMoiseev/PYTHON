from abc import ABC, abstractmethod


class IProcessor(ABC):

    @abstractmethod
    def process(self):
        ...


class Transmitter(IProcessor):

    def __init__(self, data):
        self.__data = data

    def process(self):
        print(f'Data {self.__data} send')


class Shell(IProcessor):

    def __init__(self, pr: IProcessor):
        self._processor = pr

    def process(self):
        self._processor.process()


class Expander(Shell):

    def __int__(self, pr: IProcessor):
        super().__init__(pr=pr)

    def process(self):
        print('Здесь расширяем функциональность класса')
        self._processor.process()
        print("Здесь тоже")


if __name__ == '__main__':
    tr = Transmitter(data='Data')
    tr.process()

    enc = Expander(pr=tr)
    enc.process()
