
class Foo:
    _instance = None
    _storage = None

    def __new__(cls, *argv, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)
            cls._instance._storage = 'storage'
        return cls._instance

    @property
    def storage(self):
        return self._storage


if __name__ == "__main__":
    f = Foo()
    v = Foo()
    print(id(f), id(v))
    print(f.storage)
    print(v.storage)

