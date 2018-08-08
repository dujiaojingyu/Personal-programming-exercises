__author__ = "Narwhale"
import os
import socket

server = socket.socket()
server.bind(('localhost',6565))
server.listen()
while True:
    conn,addr = server.accept()
    print('新地址：',addr)
    while True:
        print('等待新命令。。。！')
        data = conn.recv(1024)

        if not data:
            print('客户端已经断开。。')
            break
        cmd_res = os.popen(data.decode()).read()          #执行data.decode()并返回字符串形式内容
        print('检测到数据大小：',len(cmd_res.encode()))   #检测数据大小由于cmd_res是字符串，所以要encode()一下
        if len(cmd_res) == 0:
            cmd_res = "没有这个命令。。。。！"
        conn.send(str(len(cmd_res.encode())).encode('utf-8'))   #send只能传送byte类型的数据
        #此处有两个send（）可能会产生粘包，即两个内容粘在一起发送过去客户端
        conn.send(cmd_res.encode('utf-8'))
        print('传送完毕。。。。！')


    server.close()
