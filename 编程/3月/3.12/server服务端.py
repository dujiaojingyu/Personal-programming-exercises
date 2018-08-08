__author__ = "Narwhale"

import socket

server = socket.socket()
server.bind(('localhost',6565))
server.listen()
conn,addr = server.accept()

data = conn.recv(1024)
print(data)
conn.send(data.upper())
server.close()