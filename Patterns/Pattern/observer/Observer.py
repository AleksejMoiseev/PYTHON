class Event(list):

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Observable:
    def __init__(self):
        self.property_change = Event()


class Person(Observable):
    def __init__(self, name: str, age: int = 0):
        super().__init__()
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        self._age = value
        self.property_change('age', value)


class RecruitmentOffice:
    def __init__(self, person: Person):
        self.person = person
        self.person.property_change.append(self.send_summons)

    def send_summons(self, name, value):
        if name == 'age':
            if value <= 18:
                print('Еще рано')
                return
            print(f"Send summon to person > {self.person.name}")
            self.person.property_change.remove(self.send_summons)


if __name__ == '__main__':
    person = Person(name='Alex')
    RO = RecruitmentOffice(person=person)
    for age in range(10, 100):
        person.age = age
