__author__ = "Narwhale"

import threading,time

event = threading.Event()

def light():
    event.set()
    count = 0
    while True:
        if count >5 and count < 10:
            event.clear()
            print('\033[41;1m红灯亮了\033[0m' )
        elif count > 10:
            event.set()
            count = 0
        else:
            print('\033[42;1m绿灯亮了\033[0m')
        time.sleep(1)
        count +=1


def car(n):
    while True:
        if event.isSet():
            print('\033[34;1m%s车正在跑！\033[0m'%n)
            time.sleep(1)
        else:
            print('车停下来了')
            event.wait()

light = threading.Thread(target=light,args=( ))
light.start()
car1 = threading.Thread(target=car,args=('Tesla',))
car1.start()