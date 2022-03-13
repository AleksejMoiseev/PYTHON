import codecs
from Employees.serializer import SerializerEmployees, KEYS


def read_data():
    with codecs.open('employees.txt', 'r', "utf_8_sig") as file:
        lines = file.readlines()
    data = []
    for s in lines:
        data.append(s[0:len(s)-1])
    return data


def serializer(lines):
    employees = []
    for line in lines:
        employee = line.split(',')
        params = dict(zip(KEYS, employee))
        employees.append(SerializerEmployees(**params))
    return employees
