__author__ = "Narwhale"

import socket,hashlib

client = socket.socket()
client.connect(('localhost',6666))
while True:
    cmd = input('>>>:').strip()
    if len(cmd) == 0:
        continue
    if cmd.startswith('get'):          #传输文件名要以get开头如：get var
        client.send(cmd.encode('utf-8'))
        file_size = client.recv(1024)
        print('服务端检测到文件大小：', int(file_size))
        client.send('可以发送数据了'.encode(encoding='utf-8'))
        file_total_size = int(file_size)
        receive_size = 0
        filename = cmd.split()[1]         #以空格分割然后取出文件名
        f = open('new_'+filename ,'wb')
        m = hashlib.md5()
        while receive_size < file_total_size:
            if receive_size - file_total_size > 1024:             #判断最后一次还剩多少就收多少
                size = 1024
            else:
                size = file_total_size - receive_size
                print(size)
            data = client.recv(size)
            m.update(data)
            receive_size += len(data)
            f.write(data)
            print(file_total_size, receive_size)
        else:
            new_file_md5 = m.hexdigest()
            print('数据接收完成！')
            f.close()
            # client.send('可以发送md5值了'.encode())
        serve_md5 = client.recv(1024)
        print('新文件md5:',new_file_md5)
        print('原文件md5:',serve_md5)


client.close()