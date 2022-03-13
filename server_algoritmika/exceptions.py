import json
from pydantic import PydanticValueError, BaseModel, validator
from typing import List, Dict, Any


class DataValueError(PydanticValueError):
    code = 'request_is_not_valid'
    msg_template = 'request is not valid, got "{wrong_value}"'


class ValidatorRequest(BaseModel):
    method: str
    args: List
    config: Dict

    def get_method(self):
        return self.method

    def get_config(self):
        return self.config

    def check_method(self):
        method = self.get_method()
        config = self.get_config()
        if method not in config:
            raise DataValueError(wrong_value=method)
        return method

    def check_args(self):
        return self.args

    def is_valid(self):
        self.check_args()
        self.check_method()


class ValidatorResponse(BaseModel):
    result: Any


class ServerResponceMsg:
    def __init__(self, client, msg):
        self.client = client
        self.msg = msg

    def get_message(self):
        return {"message": self.msg}

    def msg_to_json(self):
        msg = self.get_message()
        return json.dumps(msg, cls=json.JSONEncoder).encode("utf-8")

    def send_msg(self):
        self.client.send(self.msg_to_json())
        self.client.close()

    def __call__(self, *args, **kwargs):
        self.send_msg()


class InvalidResponce(ServerResponceMsg):
    def __init__(self, method=None,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = method

    def get_message(self):
        return {
            "message": [
                {
                    "method": self.method,
                    "msg": self.msg
                }
            ]
        }


class SucssesResponce(ServerResponceMsg):
    def get_message(self):
        return self.msg

