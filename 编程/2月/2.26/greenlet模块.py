__author__ = "Narwhale"

from greenlet import greenlet

def fun1():
    print(6)
    gar2.switch()    #转换到gar2
    print(58)

def fun2():
    print(54)
    gar1.switch()


gar1 = greenlet(fun1)       #启动协程
gar2 = greenlet(fun2)
gar1.switch()