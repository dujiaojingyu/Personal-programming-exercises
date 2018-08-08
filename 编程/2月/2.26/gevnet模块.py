__author__ = "Narwhale"
import gevent

def fun1():
    print('第一次运行fun1')
    gevent.sleep(2)
    print('第二次运行fun1')
def fun2():
    print('第一次运行fun2')
    gevent.sleep(1)
    print('第二次运行fun2')
def fun3():
    print('第一次运行fun3')
    gevent.sleep(2)
    print('第二次运行fun3')
gevent.joinall( [
    gevent.spawn(fun1),
    gevent.spawn(fun2),
    gevent.spawn(fun3)
])