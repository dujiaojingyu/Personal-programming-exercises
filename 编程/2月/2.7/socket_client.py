__author__ = "Narwhale"

import socket

client = socket.socket()     #声明socket类型，同时生成socket连接对象

client.connect(('localhost',6565))

client.send(b'holle world!')           #传送数据只能用byte类型
data = client.recv(1024)               #一次接受的量为1024


print('recv:',data)

client.close()
