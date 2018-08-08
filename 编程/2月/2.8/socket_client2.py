__author__ = "Narwhale"

import socket

client = socket.socket()
client.connect(('localhost',6565))
while True:
    mag = input('>>>>:')
    if not mag:
        break
    client.send(mag.encode(encoding='utf-8'))
    data = client.recv(1024)
    print(data)

