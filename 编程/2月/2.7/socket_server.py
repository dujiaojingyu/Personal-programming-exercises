__author__ = "Narwhale"

import socket


server = socket.socket()
server.bind(('localhost',6565))
server.listen()       #监听
conn,addr = server.accept()     #等待

data = conn.recv(1024)

print('recv:',data)

conn.send(data.upper())
server.close()
