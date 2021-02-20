import yaml
from io import StringIO  # Введет себя как stream обьукт , т.е как файл но таким не является, т.е с ним можно
# вести себя как с файлом и методы такие же

with open("yaml.txt", "rt") as file:
    data = yaml.safe_load(file)  # функция safe_load(file) позволяет считывать файл если строка возвращает str
    # если данные подаются как name: "Aleksej" то возващвет dict
print(type(data['age']))  # доступ к данным как через словарь

# сохранение файла в yaml
with open("yaml2.txt", "wt") as file:
    yaml.dump(data=data, stream=file)  # функция dump(data=data, stream=file) сохраняет данные data в file

str_obj = "Какой то текст"
stream_obj = StringIO(str_obj)
