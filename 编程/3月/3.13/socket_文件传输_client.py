__author__ = "Narwhale"
import socket,os

client = socket.socket()
client.connect(('localhost',6565))

while True:
    cmd = input('-->>>').strip()
    if len(cmd) == 0:
        continue
    if cmd.startswith('get'):
        client.send(cmd.encode())
        file_size = client.recv(1024)
        print('检测到文件打大小',file_size.decode())
        client.send('可以发送数据了'.encode())
        file_total_size = int(file_size)
        receive_size = 0
        filename = cmd.split()[1]
        f = open('new_'+filename,'wb')
        while file_total_size > receive_size:
            if file_total_size - receive_size > 1024:
                size = 1024
            else:
                size = file_total_size - receive_size
            data = client.recv(size)
            f.write(data)
            receive_size += len(data)
            print(file_total_size, receive_size)

        else:
            print('数据接收完成！')
            f.close()
    client.close()