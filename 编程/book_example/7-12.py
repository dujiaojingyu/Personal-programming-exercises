# 程序 7-12  (Python 3 Version)
import os, sys
try:
    os.remove('hello.txt')
except Exception as e:
    print(e)
    e_type, e_value, e_tb = sys.exc_info()
    print("种类：{}\n消息：{}\n信息：{}".format(e_type, e_value, e_tb))
