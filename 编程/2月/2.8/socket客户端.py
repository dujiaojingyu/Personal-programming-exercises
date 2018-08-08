__author__ = "Narwhale"

import socket

client = socket.socket()
client.connect(('localhost',6565))
f = open('new_video.avi','wb')
while True:
    # mag = input('>>>>:')
    # if not mag:
    #     continue
    # client.send(mag.encode(encoding='utf-8'))
    data = client.recv(10240000)
    f.write(data)
    f.flush()
    if not data:
        print('接收完成。。。。。!')
        break
