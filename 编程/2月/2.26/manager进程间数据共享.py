__author__ = "Narwhale"

from multiprocessing import Manager,Process
import os

def f(d,l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l,d)

if __name__ == '__main__':
    manager = Manager()
    d = manager.dict()
    l = manager.list(range(5))
    p_list = []
    for i in range(10):
        p = Process(target=f,args=(d,l))
        p.start()
        p_list.append(p)
    for r in p_list:
        p.join()
    print(l)
    print(d)