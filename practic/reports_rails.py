"""
Создать обьект Самолет и серилизовать его в различных форматах
"""
import csv
import pandas as pd

class Reports:

    def __init__(self, factory, year):
        self.factory = factory
        self.year = year

    def to_csv(self):
        with open("airplane.csv", "wt") as file:
            csv_counter = csv.DictWriter(f=file, fieldnames=self.__dict__.keys())  # записываем в качестве имена полей
            # ключи dict что является переменными в инстансе : fieldnames=self.__dict__.keys()
            csv_counter.writeheader()  # делаем заголовок
            csv_counter.writerow(self.__dict__)

    @classmethod
    def from_csv(cls, path_csv):
        with open(path_csv, "rt") as file:
            dict_reader = csv.DictReader(file)
            line = next(dict_reader)
        return cls(**line)

if __name__ == '__main__':
    # a = [1, 2]
    # b = [3, 4]
    # reports = Reports(factory=a, year=b)
    # reports.to_csv()
    cities = pd.DataFrame([('Sacramento', 'California'), ('Miami', 'Florida')], columns=['City', 'State'])
    cities.to_csv('cities.csv', index=False)