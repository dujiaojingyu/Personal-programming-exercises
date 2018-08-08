__author__ = "Narwhala"

import time
def consumer(name):
    print('%s来了，准备吃包子！！'%name)
    while True:
        baozi = yield

        print('%s的包子来了，被%s吃掉了'%(baozi,name))

# c = consumer('Narwhala')
# c.__next__()
# c.send('猪肉馅')

def producer(name):
    c1 = consumer('A')     #只是把consumer()变成生成器
    c2 = consumer('B')
    c1.__next__()           #只有__next__()才会往下走：print('%s来了，准备吃包子！！'%name) 遇到yield会停止运行
    c2.__next__()
    print('%s要开始做包子了！'%name)

    for i in range(10):
        time.sleep(1)
        print('----------------------------')
        print('%s做好了两个猪肉馅的包子!' % name)
        c1.send('猪肉馅')
        c2.send('猪肉馅')

producer('hsj')