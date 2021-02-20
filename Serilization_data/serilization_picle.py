"""
pickle позволяет сохранять данные в байтовом формате в том числе и классы
"""
import pickle
import json

with open("json.txt", "rt") as file:
    data = json.load(fp=file)
print(data)  # получили объект data и запишем его теперь в битах и восстановим потом

with open("pickle.txt", "wb") as file:
    pickle.dump(obj=data, file=file)  # функция pickle.dump(obj=data, file=file) записывает data в file в бинарном коде

with open("pickle.txt", "rb") as file:
    data_pickle = pickle.load(file=file)
print(f" восстановили объект: {data_pickle}")


class NewClass:  # написали класс
    pass


with open("pickle1.txt", "wb") as file:
    pickle.dump(obj=NewClass(), file=file)  # записали inst класса в file

with open("pickle1.txt", "rb") as file:
    new_class_obj = pickle.load(file=file)  # восстановили объект класса NewClass
print(new_class_obj)

data_text = "i write text"
with open("pickle3.txt", "wb") as file:
    pickle.dump(obj=data_text, file=file)