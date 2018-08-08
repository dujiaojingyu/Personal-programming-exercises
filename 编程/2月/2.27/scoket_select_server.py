__author__ = "Narwhale"
import select,socket,queue

server = socket.socket()
server.bind(('localhost',9999))
server.listen()
server.setblocking(0)
inputs = [server,]  #传入select中要有链接，第一个链接是本身，监测是否来新链接
outputs = []
while True:
    realable,writeable,execptional = select.select(inputs,outputs,inputs)  #传入三个参数，返回三个结果，第一个是活动的链接，第三是出错的链接，第二不知道
    print(realable)
    for r in realable:
        if r is server:
            conn,addr = server.accept()
            print(conn)
            inputs.append(conn)  # 来了新链接，加入到监测列表中
            print('来了新链接。。。')
        else:
            data = r.recv(1024)
            print('数据：',data)
            r.send(data)
            print('send done.....')

