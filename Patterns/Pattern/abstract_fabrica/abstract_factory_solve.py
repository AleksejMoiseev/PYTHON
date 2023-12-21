from abc import ABC, abstractmethod

# Абстрактные продукты
class CarBody(ABC):
    car_body = None

# Абстрактные продукты
class Car(ABC):
    wheels = 4
    brand = None

    def __init__(self, engine, transmission):
        self.engine = engine
        self.transmission = transmission

    @abstractmethod
    def start_engine(self):
        pass

    @classmethod
    def get_brand(cls):
        return cls.brand

    def __str__(self):
        return f'{self.get_brand()}'

# Конкретные продукты
class Lada(Car):
    brand = 'Lada'

    def start_engine(self):
        print('Вставляю ключ и завожу поворотом ключа')

# Конкретные продукты
class Jeep(CarBody):
    car_body = "Jeep"


class Sedan(CarBody):
    car_body = "Sedan"


class SUV(CarBody):
    car_body = "SUV"


class LadaJeep(Lada, Jeep):
    pass


class LadaSUV(Lada, SUV):
    pass


class LadaSedan(Lada, Sedan):
    pass

# Абстрактная фабрика
class CarsFactory(ABC):

    @abstractmethod
    def create_sedan(self):
        pass

    @abstractmethod
    def create_SUV(self):
        pass

    @abstractmethod
    def create_jeep(self):
        pass

# Конкретная фабрика
class LadaCarsFactory(CarsFactory):
    def create_sedan(self, *args, **kwargs):
        return LadaSedan(*args, **kwargs)

    def create_SUV(self, *args, **kwargs):
        return LadaSUV(*args, **kwargs)

    def create_jeep(self, *args, **kwargs):
        return LadaJeep(*args, **kwargs)


if __name__ == '__main__':
    factory = LadaCarsFactory()
    jeep = factory.create_jeep(engine='gazolin', transmission='AT')
    print(jeep.car_body)