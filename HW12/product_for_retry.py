
"""
Имплементация класса Product и retrieve_product()
"""
import uuid
import random
import yaml
import xml.etree.ElementTree as ET
import json


class Product:

    def __init__(self, name, identifier):
        self._name = name
        self._identifier = identifier
        self._format = ''

    @property
    def name(self):
        return self._name

    @property
    def identifier(self):
        return self._identifier

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        self._format = value

    @classmethod
    def product(cls):
        name = random.choice(("Milk", "Water", "Bread"))
        identifier = int(uuid.uuid4())
        return cls(name=name, identifier=identifier)

    def __str__(self):
        return f"Ваш продукт : {self.name} id={self.identifier}"

    def to_yaml(self):
        data = {'name': self.name, 'identifier': self.identifier}
        return repr(data)

    @classmethod
    def from_yaml(cls, yaml_str):
        object_eval = yaml.safe_load(yaml_str)
        return cls(**object_eval)

    def to_json(self):
        data = {'name': self.name, 'identifier': self.identifier}
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

    def to_xml(self):
        product = ET.Element("product")
        name = ET.SubElement(product, "name")
        identifier = ET.SubElement(product, "identifier")
        name.text = self.name
        identifier.text = str(self.identifier)
        return ET.tostring(product, encoding="unicode")

    @classmethod
    def from_xml(cls, xml_str):
        data = {}
        root = ET.fromstring(xml_str)
        for child in root:
            data[child.tag] = child.text
        return cls(**data)

    def choice_to_serialization(self):
        choice_format = random.choice((self.to_yaml, self.to_xml, self.to_json))
        self.format = choice_format.__name__
        return choice_format()

    @classmethod
    def choice_from_serialization(cls, str_for_serialization, str_format):
        if str_format == 'to_xml':
            return cls.from_xml(xml_str=str_for_serialization)
        elif str_format == 'to_yaml':
            return cls.from_yaml(yaml_str=str_for_serialization)
        elif str_format == 'to_json':
            return cls.from_json(json_str=str_for_serialization)
        else:
            return None


class NothingToRetrieveException(Exception):
    pass


def retrieve_product():
    rand_num = random.randint(a=1, b=10)
    if rand_num % 2 == 0:
        product_to_create = Product.product()
        set_product_in_str = product_to_create.choice_to_serialization()
        dict_for_return = {
            'format': product_to_create.format,
            'serialized_str': set_product_in_str
        }
        return dict_for_return
    raise NothingToRetrieveException()


if __name__ == '__main__':
    t = Product.product()
    # str_json = t.to_json()
    # print(str_json)
    # fr_json = t.from_json(str_json)
    # print(fr_json)
    # choice = t.choice_to_serialization()
    # str_obj = t.choice_to_serialization()
    # str_format = t.format
    # print(str_obj)
    # print(str_format)
    # print(Product.choice_from_serialization(str_format=str_format, str_for_serialization=str_obj))
    # obj_dict = t.to_yaml()
    # new_obj = Product.from_yaml(yaml_str=obj_dict)
    # print(new_obj.format)
    # obj = t.to_xml()
    # print(type(obj))
    # obj_xml = xml.dom.minidom.parseString(obj)
    # print(obj_xml)
    # print(type(yaml.__name__))
    # print(retrieve_product())
