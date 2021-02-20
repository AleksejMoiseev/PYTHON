import csv

with open("text.txt", "rt") as file:
    text_csv = csv.reader(file)  # Открываем файл для чтения функцией reader(file)
    for line in text_csv:  # Каждая строчка файла представляет из себя list
        print(line)  # Читаем каждую строчку и печатаем как list

with open("text.txt", "rt") as file:
    text_csv = csv.DictReader(file)  # позволяет считывать csv файл не как list, а как dict
    for row in text_csv:
        print(row)

iterable = ["fedor", "Jovanovich", 1980]
with open("text.txt", "wt") as file:
    text_csv = csv.writer(file)  # Открываем файл для записи
    text_csv.writerow(iterable)

"""  
используем функцию writerow для записи list который представляет из себя строку
или функцию writerows  которая принимает на себя list(liskov) и пишет несколько строк
каждая из которых представляет из себя отдельный list
"""