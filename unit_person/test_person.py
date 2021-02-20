from unit_person.init_Person2 import Person, NameTooLong
import unittest
from datetime import date


class TestPerson(unittest.TestCase):

    def setUp(self) -> None:
       pass

    def test_basic(self):
        expected_name = "Fedor"
        expected_date = date(year=1979, month=8, day=3)
        fedor = Person(name=expected_name, birth_day=expected_date)

        self.assertEqual(fedor.name, "Fedor")
        self.assertEqual(fedor.birth_day, expected_date)

    def test_age(self):
        expected_name = "Fedor"
        expected_date = date(year=1979, month=8, day=3)
        fedor = Person(name=expected_name, birth_day=expected_date)

        self.assertEqual(fedor.age, 41)

    def test_check_name_too_long(self):
        expected_name = "Fedor"*11
        expected_date = date(year=1979, month=8, day=3)

        with self.assertRaises(expected_exception=NameTooLong):
            fedor = Person(name=expected_name, birth_day=expected_date)


if __name__ == '__main__':
    unittest.main()

