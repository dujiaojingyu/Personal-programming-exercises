__author__ = "Narwhale"

import socket

client = socket.socket()

client.connect(('localhost',6565))

client.send(b'hhhhhh')

data = client.recv(1024)
print(data)
client.close()