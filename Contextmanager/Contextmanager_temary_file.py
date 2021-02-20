"""
Contextmanager которые создает временные файлы
"""


import tempfile  # импорт библиотеки для работы с временными файлами

with tempfile.NamedTemporaryFile(mode="w", suffix="tmp") as file:  # Создаем временный файл через
    # tempfile.NamedTemporaryFile с mode = w и расширением  suffix="tmp"
    file.write("Записываем во временный файл информацию")  # Используем временный файл
    print('Временный файл', file.name)  # выводим для контроля на печать
    # временный файл самоуничтожился