__author__ = "Narwhale"

import re
a = '123dsjkfh54'
#将正则表达转变成一个对象
reobject1 = re.compile('\d+')

res = reobject1.findall(a)
print(res)