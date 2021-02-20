"""
распостраненные контектс менеджеры
closing - чтобы не забыть делать close()
suppress - когда у нас известно что произойдет эксепшен, можно протгнорировать эксепт
Singleton - одиночка определяет возможность создать только один инстанс класса
порождающий шаблон проектирования гарантирующий , что в однопоточном приложении
будет единственный экземпляр некоторого класса и предоставляет глобальную точку доступа к жтому экземпляру
__new__ - позволяет нам изменить как создается обьект из класса
"""


class Singleton(object):
    _instance = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


class SiSingleton2:  # подобие синглтона, но не сигналтон по определению
    name = ''
    last_name = ""

s1 = Singleton()
print("Object created", s1)
s2 = Singleton()
print("Obj created", s2)
