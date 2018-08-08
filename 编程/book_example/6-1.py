# 程序 6-1.py (Python 3.x version)
# _*_ coding: utf-8 _*_

def add2number(a, b):
    global d
    c = a + b
    d = a + b
    print("在函数中，(c={}, d={})".format(c,d))
    return c

c = 10
d = 99
print("调用函数，(c={}, d={})".format(c,d))
print("{} + {} = {}".format(2, 2, add2number(2, 2)))
print("函数调用后，(c={}, d={})".format(c,d))

  
