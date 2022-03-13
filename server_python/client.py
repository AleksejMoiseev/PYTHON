import socket
import json
"""
Client
"""
data = {
  "method": "upper",
  "args": [
    'alex',
  ]
}
data_to_json = json.dumps(data).encode('utf-8')


port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port.connect(("127.0.0.1", 8888))
port.send(data_to_json)
res = port.recv(1024)
data_from_json = json.loads(res)
print(data_from_json)
port.close()
