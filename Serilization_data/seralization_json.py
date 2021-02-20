import json
import yaml

with open("yaml.txt", "rt") as file:
    data = yaml.safe_load(file)
print(data)

with open("json.txt", "wt") as file:
    json.dump(data, file)  # функция json.dump(data, file) позволяет записать данные data в файл file

with open("json.txt", "rt") as file:
    data_json = json.load(file)  # функция  json.load(file) позволяет считывать из файла данные записанные в формате dic
print(data_json)