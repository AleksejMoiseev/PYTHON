import pickle
import json
from Serilization_data.practics_task import Airplane
"""
Записали обьект в одном файле, а восстановили в другом, предварительно импортировав его class
"""

class B:
    pass


with open("airplane.pickle", "wb") as file:
    pickle.dump(obj=B(), file=file)

with open("airplane.txt", "rb") as file:
    new_obj_pickle = pickle.load(file=file, encoding="utf8")
with open("airplane.json", "rt") as file:
    new_obj_json = json.load(file)
print(new_obj_json)