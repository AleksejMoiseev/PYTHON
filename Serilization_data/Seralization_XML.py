"""
XML - формат основан на HTML tags
"""
import xml.etree.ElementTree as ET
import xml.dom.minidom


class Person:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def dump_to_xml(self):  # Метод который превращает обьект person  в XML
        person = ET.Element("person")  # Создает тег "person"
        name = ET.SubElement(person, "name")  # Добавляет элемент "name" как дочерний
        last_name = ET.SubElement(person, "last_name")  # Добавляет элемент "name" как дочерний
        birth_year = ET.SubElement(person, "birth_year")   # Добавляет элемент "name" как дочерний
        name.text = self.name  # добавляет в тег текст в качестве текста подставляется значение self.
        last_name.text = self.last_name  # добавляет в тег текст в качестве текста подставляется значение self.
        birth_year.text = str(self.birth_year)  # добавляет в тег текст в качестве текста подставляется значение self.
        return person  # возвращает тег person вместе с дочерними элементами


if __name__ == '__main__':
    alex = Person(name="Aleksej", last_name="Moiseev", birth_year=1979)
    bentsi = Person(name="Bentsi", last_name="Magitovich", birth_year=1985)
    xml_alex = alex.dump_to_xml()  # создаем XML обьект
    xml_bentsi = bentsi.dump_to_xml()
    department = ET.Element("depatment")  # Создаем тег depatment
    department.append(xml_alex)  # добавляем в него XML обьект
    department.append(xml_bentsi)
    result = ET.tostring(department)  # функция ET.tostring превращает обьект XML в строку
    dom = xml.dom.minidom.parseString(result)  # функция позволяет получить красивую печать
    print(dom.toprettyxml())  # Вывод красивой печати
"""
результат программы:

b'<depatment>
	<person>
		<name>Aleksej</name>
		<last_name>Moiseev</last_name>
		<birth_year>1979</birth_year>
	</person>
	<person>
		<name>Bentsi</name>
		<last_name>Magitovich</last_name>
		<birth_year>1985</birth_year>
	</person>
</depatment>'
"""