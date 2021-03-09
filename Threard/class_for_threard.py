import threading
import time
from concurrent.futures import ThreadPoolExecutor


class MyRunningThreadBase(threading.Thread):  # Наследуем от класса и нужные параметры передаем в констрактор

    def __init__(self, sleep_to, daemon):
        super().__init__(daemon=daemon)  # определяем daemon=daemon, для понимания завершения параллельных процесоов
        # по окончании главного процесса
        self.sleep_to = sleep_to

    def run(self):
        print("threard starting")
        time.sleep(self.sleep_to)
        self.handle()
        print("threard finishing")

    def handle(self):
        raise NotImplementedError()


class Handler1(MyRunningThreadBase):  # Наследуем от класса и нужные параметры передаем в констрактор
    def handle(self) -> None:  # Метод для описании логики процесса которому бежать парралельно
        print("handle")


def start_threard(name):
    print(f"start threard {name}")
    time.sleep(1)
    print(f"finish threard {name}")
    return name

def func(n ,m):
    print(n, m)


if __name__ == '__main__':
    # print("start main threid")
    # threard = Myrunningthread(sleep_to=5, daemon=True)
    # threard.start()  # Стартуем параллельный процесс
    # print()
    # print("Снова бежим ")
    # threard.join(timeout=2)  # завершаем JOIN все параллельные процессы программа ждет время равное timeout=2
    # print("cyjdf main")
    # print("main finish")
    # with ThreadPoolExecutor(max_workers=3) as EX:
    #     result = EX.map(start_threard, [2, 3])
    # print(result)
    d = {'n': 2, 'm': 3}
    func(**d)






