"""
Создание Contextmanager через класс
с его помощью мы декорируем блок кода
"""
from contextlib import ExitStack


class Contextmanager:

    def __init__(self):  # При создании Contextmanager __init__ убрать если он не нужен,
        # важны только методы __enter__ и __exit__
        print("запускается какой то первоначальный код init")

    def __enter__(self):  # первоначальная инструкция возвращает обьект Contextmanager в CM
        print("Запускается после кода в init, какая то инструкция которая должна выполнится " )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # запускается после основного блока кода для завершения программы
        print("Запускается после основного блока программы и завершает ее выполнение этим кодом")


with ExitStack() as stack:                 # позволяет запускать несколько Contextmanager на основе stack,
                                           # встроеный from contextlib import ExitStack по принципу
                                           # последний вошел первый вышел
    stack.enter_context(Contextmanager())  # Запускается последним через stack.enter_context
    stack.enter_context(Contextmanager())  # Запускается и выполняется вторым через stack.enter_context
    stack.enter_context(Contextmanager())  # Запускается и выполняется первым через stack.enter_context
    print("И наконец основной код")
print("Конец балала балала йка")


if __name__ == '__main__':
    with Contextmanager() as CM:
        print("Основной блок кода запускается здесь")