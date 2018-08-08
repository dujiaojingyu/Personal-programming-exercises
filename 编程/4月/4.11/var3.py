__author__ = "Narwhale"
import json

def input_num():
    '''输入数字'''
    num = input('请输入您喜欢的数字：')
    with open('num.txt','w') as f_obj:
        json.dump(num,f_obj)

def read_file():
    with open('num.txt', 'r') as f_obj:
        num = json.load(f_obj)
        print('I konw your favorite number!It\'s %s'%num)

input_num()
read_file()