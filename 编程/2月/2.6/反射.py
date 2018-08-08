__author__ = "Narwhale"

# class Dog(object):
#
#     def __init__(self,name):
#         self.name = name
#
#     def eat(self):
#         print('%s is eating ....'%self.name)
#
# d = Dog('xiaohei')                     #实例化对象
# choice = input('>>>>:').strip()      #strip()去除左右空格
#
# if hasattr(d,choice):                #检查实例化d中有没有choice
#     func = getattr(d,choice)         #getattr返回d中的choice的内存地址
#     func()                            #执行函数
#

class Foo(object):

    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        return 'func'


obj = Foo()

# #### 检查是否含有成员 ####
hasattr(obj, 'name')
hasattr(obj, 'func')

# #### 获取成员 ####
getattr(obj, 'name')
getattr(obj, 'func')

# #### 设置成员 ####
setattr(obj, 'age', 18)
setattr(obj, 'show', lambda num: num + 1)

# #### 删除成员 ####
delattr(obj, 'name')
delattr(obj, 'func')

