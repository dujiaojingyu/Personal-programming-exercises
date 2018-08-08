__author__ = "Narwhale"
import queue,time,threading
q = queue.Queue(10)

def producer(name):
    count = 0
    while True:
        print('%s生产了包子%s'%(name,count))
        q.put('包子%s'%count)
        count += 1
        time.sleep(1)

def consumer(name):
    while True:
        print('%s取走了[%s],并且吃了它。。。。。'%(name,q.get()))
        time.sleep(1)


A1 = threading.Thread(target=producer,args=('A1',))
A1.start()

B1 = threading.Thread(target=consumer,args=('B1',))
B1.start()
B2 = threading.Thread(target=consumer,args=('B2',))
B2.start()


