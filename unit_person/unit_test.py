
"""
#!/usr/bin/env python - устанавливаем, чтобы можно было запускать из терминала файл unit_test.py
и интерпретатор понимал, что ему использовать для интерпретирования файла
далее прописываем в терминале  chmod +x unit_test.py
где имя файла == unit_test.py, и после можем запускать
./unit_test.py
"""
"""
Unit test это тест который создается на единицу продукта, метод, функцию, класс, самую маленькую единицу
integration test  это тест на все приложения, пэкэджи и т.д
 нужен фреймоворк чтобы иметь возможность запустить все тесты и потом предоставлять нам отчет,
   а также имеет другие функциональности 
   группируем тесты в  тест кейс
   для запуска в терминале надо набрать: chmod+x name.file
                                         ./name.file
для запуска 1 теста : python3 -m unittest name.file
c запуском verbose mod чтобы все видеть: python3 -m unittest -v name.file
"""


import unittest


class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Метод который запускается один раз перед запуском всего класса, содержащих все тесты")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Запускается один раз после выполнения всех тестов в классе")

    def setUp(self) -> None:
        print("Запускается перед каждым методом класса")

    def tearDown(self) -> None:
        """
        Результат:
        Метод который запускается один раз перед запуском всего класса, содержащих все тесты
        test_isupper (unit_test.TestStringMethods) ... Запускается перед каждым методом класса
        Запускается после каждого метода класса
        ok
        test_split (unit_test.TestStringMethods) ... Запускается перед каждым методом класса
        Запускается после каждого метода класса
        ok
        test_upper  (unit_test.TestStringMethods) ... Запускается перед каждым методом класса
        Запускается после каждого метода класса
        skipped 'Fixing bugs'
        Запускается один раз после выполнения всех тестов в классе

        """
        print("Запускается после каждого метода класса")

    def test_upper(self):  # Все тесты начинаются с test_, так распознаются и запускаются тесты
        self.skipTest(reason="Fixing bugs")  # Позволяет пропустить тест если в нем
        # баг и мы хотим его пока исключить из проверки в reason записываем комментарий
        test_string = "foo"
        # assert "foo".upper() == "FOO", f"{test_string} should be uppercase"
        self.assertEqual('foo'.upper(), 'FOo', msg=f"{test_string} should be uppercase")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Проверим, что s.split не работает, если разделитель - не строка
        with self.assertRaises(TypeError):
            s.split(2)
"""
запуск теста через терминал обычный -  python  unit_test.py
"""

"""
Сначала прописывается chmod+x name.file
далее запуск всегда можно как : ./unit_test.py
"""

"""
если мы хотим запустить только конкретный тест из всего класса
например: test_isupper
прописываем команду: 

python -m unittest unit_test.TestStringMethods.test_isupper
"""

"""
Для запуска теста verbose ( подробно)

python -m unittest -v unit_test.py
результат:
test_isupper (unit_test.TestStringMethods) ... ok
test_split (unit_test.TestStringMethods) ... ok
test_upper (unit_test.TestStringMethods) ... FAIL
 

"""


if __name__ == '__main__':
    unittest.main()