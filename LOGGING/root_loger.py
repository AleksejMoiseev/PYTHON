import logging  # Импортируем модуль logging

LOGGER = logging.getLogger(__name__)

def setup_logging():
    file_handler = logging.FileHandler("/tmp/my_logging.log")  # Определяем файл в который собираемся писать log
    formatter = logging.Formatter("[%(asctime)s] - %(levelname)s - %(message)s")  # задаем формат дога
    file_handler.setFormatter(fmt=formatter)  # добавляем формат в handler
    file_handler.setLevel(level=logging.DEBUG)  # определяем с какого уровня начинаем писать логи

    root_logger = logging.getLogger()
    root_logger.addHandler(hdlr=file_handler)
    root_logger.setLevel(level=logging.DEBUG)



def func():
    print('1')
    LOGGER.info(msg="Я пишу сообщщение")


if __name__ == '__main__':
    setup_logging()
    func()
