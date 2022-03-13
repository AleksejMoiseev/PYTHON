import json
import socket
import threading

from Mark_lutc.func_for_check import add, sub, upper
from server_algoritmika.exceptions import ServerResponceMsg
from server_algoritmika.helpers import _make_config

list_funcs = [add, sub, upper]
CONFIG = _make_config(list_funcs)


class ServerHandler(threading.Thread):
    def __init__(self,client, config, *args, **kwargs):
        super().__init__(daemon=True, *args, **kwargs)
        self.registered_procedure = config
        self.client = client

    def get_name_procedure(self, procedure):
        if not (type(procedure) != 'function'):
            ServerResponceMsg(msg='Procedure dont functions', client=self.client)
        return procedure.__name__

    def register_function(self, procedure):
        procedure_name = self.get_name_procedure(procedure)
        self.registered_procedure[procedure_name] = procedure

    def run(self) -> None:
        data = json.loads(self.client.recv(1024))
        if not self.is_valid(data):
            ServerResponceMsg(client=self.client, msg='Data not is valid')
        key = data['method']
        args = data["args"]
        resp = "INVALID PARAMS ARG"
        try:
            result = self.registered_procedure[key](*args)
            resp = {
                'result': result
            }
        except Exception:
            ServerResponceMsg(client=self.client, msg=resp)
        finally:
            ServerResponceMsg(client=self.client, msg=resp)
            self.client.close()

    def set_client(self, client):
        self.client = client

    def is_valid(self, data):
        method = data['method']
        if method not in self.registered_procedure:
            return False
        return True


def start_server(config) -> None:
    port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создали сокет
    port.bind(("127.0.0.1", 8888))  # Зарезервировали порт
    port.listen(2)  # Создали возможность очереди
    while True:
        try:
            client, addr = port.accept()  # Присоединились к форме
            handler = ServerHandler(config=config, client=client)
            handler.start()
        except KeyboardInterrupt:
            port.close()
            break


if __name__ == '__main__':
    start_server(config=CONFIG)




