import json


class ServerResponceMsg:
    def __init__(self, client, msg):
        self.client = client
        self.msg = msg
        self.send_msg()

    def msg_to_json(self):
        msg = {"message": self.msg}
        return json.dumps(msg, cls=json.JSONEncoder).encode("utf-8")

    def send_msg(self):
        self.client.send(self.msg_to_json())
        self.client.close()
