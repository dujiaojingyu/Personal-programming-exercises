__author__ = "Narwhale"
import json

try:
    with open('num.txt', 'r') as f_obj:
        num = json.load(f_obj)
except FileNotFoundError:
    num = input('请输入您喜欢的数字：')
    with open('num.txt', 'w') as f_obj:
        json.dump(num, f_obj)
        print('I konw your favorite new number!It\'s %s'%num)
else:
    print('I konw your favorite old number!It\'s %s'%num)
