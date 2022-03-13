import json
import socket
import threading

from Mark_lutc.func_for_check import add, sub, upper
from server_algoritmika.exceptions import ServerResponceMsg, DataValueError, InvalidResponce, SucssesResponce
from server_algoritmika.exceptions import ValidatorRequest, ValidatorResponse
from server_algoritmika.helpers import make_config

list_funcs = [add, sub, upper]
CONFIG = make_config(list_funcs)


class ServerHandler(threading.Thread):
    def __init__(self, client, config, *args, **kwargs):
        super().__init__(daemon=True, *args, **kwargs)
        self.registered_procedure = config
        self.client = client
        self.cleaned_data = None

    @property
    def cleaned_data(self):
        return self.__cleaned_data

    @cleaned_data.setter
    def cleaned_data(self, value):
        self.__cleaned_data = value

    def run(self) -> None:
        data = json.loads(self.client.recv(1024))
        if self.is_valid(params=data):
            data = self.cleaned_data
            resp = self.get_result(data=data)
            SucssesResponce(client=self.client, msg=resp)()
            self.client.close()
        else:
            InvalidResponce(client=self.client, msg="Unhandled errors occurred")

    def set_client(self, client):
        self.client = client

    def validators(self, params):
        try:
            data = ValidatorRequest(config=self.registered_procedure, **params)
            data.is_valid()
            return True, data
        except DataValueError as exc:
            resp = ValidatorResponse(result=exc.code)
            InvalidResponce(client=self.client, msg=resp.json(), method=params.get('method', "Method not found"))()
            return False, params

    def is_valid(self, params):
        is_valid, data = self.validators(params)
        if is_valid:
            self.cleaned_data = data
            return True
        self.cleaned_data = None
        return False




    def get_result(self, data):
        key = data.method
        args = data.args
        try:
            result = self.registered_procedure[key](*args)
            obj = ValidatorResponse(result=result)
        except Exception:
            obj = ValidatorResponse(result="INVALID PARAMS ARG")
        return obj.json()


def start_server(config, http_host, http_port) -> None:
    port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port.bind((http_host, http_port))
    port.listen(3)
    while True:
        try:
            client, address = port.accept()
            handler = ServerHandler(config=config, client=client)
            handler.start()
        except KeyboardInterrupt:
            port.close()
            break


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8888
    start_server(config=CONFIG, http_host=host, http_port=port)
