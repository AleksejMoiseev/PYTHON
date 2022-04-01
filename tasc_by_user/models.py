from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str

    @classmethod
    def serializer(cls, data: str):
        keys = cls.__fields__.keys()
        values = tuple(data.split())
        params = dict(zip(keys, values))
        return cls(**params)

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age
