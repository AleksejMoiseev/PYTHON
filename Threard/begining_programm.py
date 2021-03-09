import threading  # Импортируем модуль для организации многопоточного программировнаия
import time


def start_threard(name):
    print(f"start threard {name}")
    time.sleep(10)
    print(f"finish threard {name}")

if __name__ == '__main__':
    print("Стартовал main threard")
    my_threard = threading.Thread(target=start_threard, args=("name_threard", ), daemon=True)  # Запускаем первый тред
    # где target это наименование функции а args это tuple её arguments,
    # !!! daemon=True Важно, при таком значении трейд заканчивает работу одновременно когда останавливается main threard
    my_threard.start()  # starting threard
    print("main running parallel with threard")
    print("Все еще бежит рядом пока выполняется функция start_threard")
    my_threard.join(timeout=11)  # Показыввает сколько нужно ждать до совершения треда
    print("Дождались")

