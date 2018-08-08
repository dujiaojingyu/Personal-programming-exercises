__author__ = "Narwhale"

import threading,time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('线程%s在跑！'%n)
    semaphore.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)      #最多5个线程同时跑
    for i in range(20):
        t = threading.Thread(target=run,args=(i,))
        t.start()

while threading.active_count() !=1:
    pass
else:
    print('所有线程跑完了！')