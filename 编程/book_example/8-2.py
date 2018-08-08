# _*_ coding: utf-8 _*_
#程序 8-2 (Python 3 version)

import sys

print("参数长度={}".format(len(sys.argv)))
i = 0
for arg in sys.argv:
    print("第{}个参数是:{}".format(i,arg))
    i += 1