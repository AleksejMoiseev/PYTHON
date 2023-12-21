
class Person:
    def __init__(self):
        # lives
        self.street = None
        self.post_cose = None
        self.house = None
        self.flat = None

        # works
        self.profession = None
        self.salary = None
        self.factory = None

    def __str__(self):
        return (f'lives: street - {self.street}, post_cose - {self.post_cose} house - {self.house} flat - {self.flat}'
                f' Works: profession - {self.profession} salary - {self.salary} factory - {self.factory}')


class PersonBuilder:
    # Текущий интерфейс при переходе от одного строителя к другому
    def __init__(self, person=Person()):
        self.person = person

    @property
    def lives(self):
        return LiveBuilder(self.person)

    @property
    def works(self):
        return JobBuilder(self.person)

    def build(self):
        return self.person

class LiveBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person=person)

    def add_street(self, street: str):
        self.person.street = street
        return self

    def add_post_cose(self, post_cose: int):
        self.person.post_cose = post_cose
        return self

    def add_house(self, house: int):
        self.person.house = house
        return self

    def add_flat(self, flat: int):
        self.person.flat = flat
        return self


class JobBuilder(PersonBuilder):

    def __init__(self, person):
        super().__init__(person=person)

    def add_profession(self, profession: str):
        self.person.profession = profession
        return self

    def add_salary(self, salary: int):
        self.person.salary = salary
        return self

    def add_factory(self, factory: str):
        self.person.factory = factory
        return self


if __name__ == '__main__':
    person = (PersonBuilder().
              lives.add_street('Pionerskay').add_flat(260).add_house(1).add_post_cose(300000).
              works.add_factory('Roga and Copyta').add_salary(20).add_profession('manager').
              build()
              )

    print(person)