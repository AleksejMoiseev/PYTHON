import socket


port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создали сокет
port.bind(("127.0.0.1", 8080))  # Зарезервировали порт
port.listen(2)  # Создали возможность очереди
try:
    client, addr = port.accept()  # Присоединились к форме
    print(client)
except KeyboardInterrupt:
    port.close()
else:
    resultat = client.recv(1024)
    print("message: ", resultat.decode('utf-8'))
    print(client.recv(1024) == False)
    client.close()


