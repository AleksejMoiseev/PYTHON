"""
Необходимо разработать две функции thread_requests и blocked_requests. В каждой из них будут отправляться запросы
на получение погоды для конкретного города. Список городов определен в глобальной переменной CITIES.
Полученную информацию о погоде (градус по Цельсию) необходимо сохранять в storage (глобальная переменная типа dict)
в формате "ключ-значение", где ключом будет выступать город, а значением - погода в градусах по Цельсию.

Отличие этих функций в том, что в thread_requests необходимо отправлять запрос в отдельном потоке,
в то время как в blocked_requests запросы отправляются синхронно и последовательно, то есть,
мы дожидаемся ответа на первый запрос перед тем как отправить второй запрос.

Разработнные функции thread_requests и blocked_requests необходимо сравнить по времени выполнения и сделать выводы.

Для работы с погодой необходимо зарегистрироваться на https://www.weatherapi.com/ и получить API KEY.
Код необходимо написать в файле weather.py.
fe797b7b88344708a1b55801221103
"""

import threading

import requests

from Decorator.measure_time import measure_time

KEY = "fe797b7b88344708a1b55801221103"
URL = "https://api.weatherapi.com/v1/current.json"

CITIES = [
    "Paris",
    "London",
    "New_York",
    "Moscow",
]

STORAGE_WEATHER = {}


def get_weather(city):
    get_params = f'q={city}&key={KEY}'
    path = f"{URL}?" + get_params
    response = requests.get(path)
    data = response.json()

    return data["current"]["temp_c"]


def add_weather(city):
    print('!!!!!!!!!!!!!!!!!')
    value = get_weather(city)
    print('!data!!!', value)
    STORAGE_WEATHER[city] = value
    print(STORAGE_WEATHER)


@measure_time
def thread_requests():
    threads = []
    for city in CITIES:
        thread = threading.Thread(target=add_weather, args=(city,))
        thread.start()
    #     threads.append(thread)
    # for thread in threads:
    #     thread.run()
    #     # thread.start()


@measure_time
def blocked_requests():
    for city in CITIES:
        STORAGE_WEATHER[city] = get_weather(city)
for city in CITIES:
    thread = threading.Thread(target=add_weather, args=(city,))
    thread.start()

if __name__ == "__main__":
    #thread_requests()
    # blocked_requests()
    print(STORAGE_WEATHER)