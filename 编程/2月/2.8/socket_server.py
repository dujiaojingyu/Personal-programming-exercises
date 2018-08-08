__author__ = "Narwhale"

import socket

server = socket.socket()
server.bind(('localhost',6565))
server.listen(5)
print('等待中。。。。。！')
while True:
    conn,addr = server.accept()
    while True:
        data = conn.recv(1024)
        print(data)
        conn.send(data.upper())

        if not data:
            print('关闭当前对话，等待下一个对话！')
            break
