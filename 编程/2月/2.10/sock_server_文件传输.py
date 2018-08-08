__author__ = "Narwhale"

import socket,os,hashlib

server = socket.socket()
server.bind(('localhost',6666))
server.listen()
conn, addr = server.accept()
while True:
    print('等待新数据！')
    cmd = conn.recv(1024)
    if len(cmd) == 0:
        break
    filename = cmd.decode().split()[1]
    print(filename)
    if os.path.isfile(filename):          #判断文件是否存在
        f = open(filename,'rb')           #打开文件
        m = hashlib.md5()
        file_size = os.stat(filename).st_size   #查询文件大小
        # file_size = os.stat(filename).st_size   #查询文件大小
        print(file_size)
        conn.send(str(file_size).encode())         #给客户端发送文件大小
        conn.recv(1024)                              #等待并接受客户端的确认，这一步可以解决粘包问题
        for line in f:                              #边读边循环发送文件
            m.update(line)                           #得出每一句的md5值
            conn.send(line)                           #发送给客户端
        print('file md5:',m.hexdigest())
        f.close()
        # conn.recv(1024)
        conn.send(m.hexdigest().encode())

    print('传送完成！')

server.close()