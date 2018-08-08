__author__ = "Narwhale"

import socket,os

server = socket.socket()
server.bind(('localhost',6565))
server.listen()

conn,addr = server.accept()
while True:
    print('等待新数据')
    cmd = conn.recv(1024)
    filename = cmd.decode().split()[1]
    print(filename)
    if os.path.isfile(filename):
        f = open(filename,'rb')
        file_size = os.stat(filename).st_size
        conn.send(str(file_size).encode())
        conn.recv(1024)
        for line in f:
            conn.send(line)
        f.close()
    print('传送完成')
    server.close()


