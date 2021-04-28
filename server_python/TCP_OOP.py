import socketserver

const = """HTTP/1.1
Host: TCP_OOP.py
Connection: keep-alive
Accept: text/html
"""
class HandlmandlTCPIPclass(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        data = self.request.recv(1024).strip()
        print("address", self.client_address)
        result = data.decode()
        print("Data", result)
        self.request.send(const.encode())
if __name__ == '__main__':
    with socketserver.TCPServer(("127.0.0.1", 8888), RequestHandlerClass=HandlmandlTCPIPclass) as sock:
        sock.serve_forever()