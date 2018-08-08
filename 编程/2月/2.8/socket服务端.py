__author__ = "Narwhale"

import socket
f = open('video.avi','rb')
server = socket.socket()
server.bind(('localhost',6565))
server.listen(5)
print('等待中。。。。。！')
conn,addr = server.accept()
while True:
    # data = conn.recv(1024)
    # print(data)
    # if not data:
    #     print('关闭当前对话，等待下一个对话！')
    #     break
    data = f.read()
    conn.sendall(data)
    if not data:
        print('传送完成......！')
        break
