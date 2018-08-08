__author__ = "Narwhale"

import socket

client = socket.socket()
client.connect(('localhost',6666))
while True:
    cmd = input('>>>:')

    if cmd == 0:
        continue

    client.send(cmd.encode('utf-8'))
    cmd_size = client.recv(1024)
    print('服务端检测到数据大小：', cmd_size)

    if len(cmd_size) !=0:
        client.send('可以发送数据了'.encode(encoding='utf-8'))

    receive_size = 0
    receive_cmd = b''

    while receive_size < int(cmd_size.decode()):
        data = client.recv(1024)
        receive_size += len(data)
        receive_cmd += data
    else:
        print('接收到数据大小：',receive_size)
        print('数据接收完成！')
        print(receive_cmd.decode())