__author__ = "Narwhale"

import socket,os

server = socket.socket()
server.bind(('localhost',6666))

server.listen()
conn, addr = server.accept()
while True:
    print('等待新数据！')
    cmd = conn.recv(1024)

    if len(cmd) == 0:
        break

    data = os.popen(cmd.decode()).read()
    cmd_size = len(data.encode('utf-8'))
    print('检测到数据大小',cmd_size)

    if len(data) == 0:
        data = '没有此命令！！'

    conn.send(str(len(data.encode('utf-8'))).encode())
    order = conn.recv(1024)

    conn.send(data.encode('utf-8'))
    print('传送完成！')

server.close()