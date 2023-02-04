"""
Создать обьект Самолет и серилизовать его в различных форматах
"""
import pickle
import json
import yaml
import csv


class Airplane:

    def __init__(self, factory, year):
        self.factory = factory
        self.year = year

    def to_pickle(self):
        with open("airplane.txt", "wb") as file:
            pickle.dump(obj=self, file=file)  # pickle умеет записывать обьекты поэтому мы передаем ему весь класс

    def __str__(self):
        result = f"Airplane: factory {self.factory} год выпуска: {self.year}"
        return result

    def to_json(self):
        with open("airplane.json", "wt") as file:
            json.dump(self.__dict__, file)  # json умеет записывать dict поэтому передаем dict через self.__dict__

    @classmethod
    def from_json(cls, path_to_json):  # json возвращает dict, его нужно распарсить и передать в класс и после вернуть
        # инстанс класса

        with open(path_to_json, "rt") as file:
            data_json = json.load(file)
        return cls(**data_json)  # разворачиваем dict и передаем в класс чтобы получить инстанс класса

    def to_yml(self):
        with open("airplane.yml", "wt") as file:
            yaml.dump(self.__dict__, file)

    @classmethod
    def from_yml(cls, path_yml):
        with open(path_yml, "rt") as file:
            data_yml = yaml.safe_load(file)
        return cls(**data_yml)

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
    airplane = Airplane(factory="Tu ", year=2020)
    # print(airplane)
    # airplane.to_pickle()
    # airplane.to_json()
    # airplane.to_yml()
    # class_json = Airplane.from_json(path_to_json="airplane.json")
    # class_yml = Airplane.from_yml(path_yml="airplane.yml")
    # print(class_yml)
    airplane.to_csv()
    # class_csv = Airplane.from_csv(path_csv="airplane.csv")
    # print(class_csv)
