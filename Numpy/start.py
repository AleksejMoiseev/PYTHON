import numpy as np

my_list = [1, 2, 3, 4, 5, 6]
# Преобразование списка в массив
my_array = np.array(my_list)

# Все числа умножены на 10
my_array = my_array * 10
print(my_array)
# Десять списков
my_list = my_list * 10
print(my_list)

my_tuple = (1, 2, 3, 4, 5, 6)
print(my_tuple * 10)

my_array = np.array(my_tuple)
print(my_array * 10)

my_arrange = np.arange(start=10, stop=20, step=2)

print(my_arrange)

### Linspase
# Раствляет 11 элементов от 10 до 30
print(np.linspace(start=10, stop=30, num=11))
print(np.linspace(start=10, stop=30, num=11).size)