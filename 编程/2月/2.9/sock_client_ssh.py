__author__ = "Narwhale"

import socket

client = socket.socket()
client.connect(('localhost',6565))
while True:
    cmd = input('>>>>:').strip()
    if len(cmd) == 0:
        continue

    client.send(cmd.encode(encoding='utf-8'))         #发送指令
    cmd_res_size = client.recv(1024)                  #第一个recv接收的是服务端检测到的数据大小
    print('检查到的数据大小：', cmd_res_size.decode())
    receive_cmd = 0
    receive_data = b''
    while receive_cmd < int(cmd_res_size.decode()):
        data = client.recv(1024)                    #第二个recv接收的是数据内容
        receive_cmd +=len(data)                     #计算接收到的数据大小
        receive_data += data

    else:
        print("数据传输完成。。！")
        print('接收到的数据大小：', receive_cmd)
        print(receive_data.decode())

    client.close()


