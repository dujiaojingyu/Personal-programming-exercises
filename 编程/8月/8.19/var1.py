__author__ = "Narwhale"

import socket
#服务端
server = socket.socket()
server.bind(('localhost',5656))
server.listen()
conn,addr = server.accept()

server_data = conn.recv()

#客户端
client = socket.socket()
client.connect(('localhost',5656))

client_data = client.recv()