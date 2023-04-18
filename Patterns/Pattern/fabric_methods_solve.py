from abc import ABC, abstractmethod


class Base(ABC):
    def get_class_name(self):
        return f'{self.__class__.__name__}'


class Weapon(Base):
    def __str__(self):
        return f'{self.get_class_name()}'

    @abstractmethod
    def shot(self):
        pass


class Soldier(Base):
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.set_shot()

    def __str__(self):
        return f'{self.get_class_name()} - {self.name}'

    def attack(self):
        if self.weapon:
            self.weapon.shot()
        else:
            print('i don`t have weapon')

    @abstractmethod
    def set_shot(self):
        pass


class Tank(Weapon):
    def shot(self):
        print('Tank shell fire')


class TankMan(Soldier):
    def set_shot(self):
        self.weapon = Tank()


if __name__ == '__main__':
    tank_man = TankMan(name='Roma')
    print(tank_man)
    tank_man.attack()
