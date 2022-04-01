import socket
import json
data = {'name': 'add'}
data_to_json = json.dumps(data).encode('utf-8')


#t = b'import requests# methodmethod_name = "crm.deal.list"# Адрес api метода для запроса get url_param = "https://domain.ru/rest/1/854984lkjdsijd432/" + method_nameparams = {"filter[>DATE_CREATE]": "2020-01-01T00:00:01+01:00"print(paramsresponse = requests.post(url_param, data = paramsresult = response.json(total = result]rint(total)'

port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port.sendto(data_to_json, ('127.0.0.1', 8888))
port.close()