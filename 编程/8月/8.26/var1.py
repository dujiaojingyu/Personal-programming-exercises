__author__ = "Narwhale"

#考察匿名函数把t1和t2合并用zip函数，再将k，v合并成字典，考察列表推导式
# t1 = (('a'),('b'))
# t2 = (('c'),('d'))

# res = lambda t1,t2:[{k:v} for k,v in (zip(t1,t2))]
# # res = lambda t1,t2:[dict(zip(t1,t2))]
# print(res(t1,t2))

################################################

#什么是匿名函数，匿名函数有什么好处？

#当我们创建函数时不需要显示的定义函数，省去了给函数起名字的麻烦，也减少了相当的代码

###################################################

#考察and 和 or

#1 and 2 ---------->2

#1 or 2------------>1

#################################################

# *args代表将位置参数打包成元组
# **kwargs代表关键字参数打包成字典
#都可以当作普通参数使用

# def func( *args, **kwargs):
#     print('args is', args)
#     print('kwargs is', kwargs)
#     return args
#
#
# f = func('hello',12,3,445,6,a=2,e=54)
# # args is ('hello', 12, 3, 445, 6)
# # kwargs is {'a': 2, 'e': 54}
# print(f[0]) --------->hello

#########################################
#生成器
# x = (i%2 for i in range(10))
# print(x) --------------->generater

###########################################

# Unicode 和 utf-8 的关系

# UTF-8就是在互联网上使用最广的一种unicode的实现方式

###################################################

#def func(a,b=[]):pass这样写函数有什么缺陷？

#python 函数被定义的时候。默认b的值就被计算出来了，即[],参数b是一个变量，它指向的对象是[]
#每次调用这个函数的时候，可如果改变了b的内容，默认参数也改变了，不再是定义时的[]，内容改变了
#所以牢记 ：默认参数必须指向不可变对象

#####################################################

#实现九九乘法
# for i in range(1,10):
#     print('\n')
#     for j in range(1,10):
#         print('%s*%s=%s'%(i,j,i*j),end=' | ')
#

#########################################################

#python标准库
#os、sys、datetime、re、match


#######################################################

#GIL全局解释器锁，同一个进程中有多线程执行时，同一时间下只能有一个线程运行

#########################################################

#单例模式
# class Single_instance(object):
#     __instance = None
#
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls, *args, **kwargs)
#         return cls.__instance
#
# a = Single_instance()
# b = Single_instance()
# print(id(a),id(b))

###############################################

#文件操作
#写入文件时最好加入encoding这样不容易出错，读取文件时也要加入encoding不然会出错

# with open('f.txt','w',encoding='utf-8') as f:
#     f.write('你好')

# f = open('f.txt','r',encoding='utf-8')
# for line in f:
#     print(line)
# #无论是写入文件读取文件都要打开一个文件，因此都要关闭文件
# f.close()

#############################################################

#匹配<div class="name">中国</div>，class内容不确定
# import re
# a = '<div class="name">中国</div>'
# res = re.compile('<div class=".*(.*)</div>')
# result = res.findall(a)
# print(result)

###########################################################

#数据有表student，表有字段id、name、score、city
#其中name中名字可有重复，需要消除重复行

#select distinct name from student


############################################################

#linux常用命令

#ls、pwd、rm、mkdir、tree、cp、touch、echo、more、mv

#########################################################
#列表可变类型

# a = [1,2,3,4,5,6,7]
# print(id(a))
# a.append(8)
# print(id(a))
#
# #字符串不可变类型
# s = 'shdkjhdfoisd'
# print(id(s))
# s = s[:4]
# print(id(s))

###################################################

# g = lambda x,y:x*y
# print(g(1,4))

#################################################
#根据键从小到排序
# dict1 = {"name":"zs","age":23,"city":"广州","tel":"1376487434"}
# res = dict1.items()
# print(res)
# s = sorted(res,key=lambda x:x[0])
# print(s)
# # dict1 = dict(s)
# #字典推导式
# dict2 = { k:v for k,v in s}
# print(dict2)

###################################################

#正则表达式过滤掉英文和数字，输出中文
#import re
# a = "not 404 found 张三 99 深圳"
# a = a.replace(' ','')
# print(a)

# re_object = re.compile('\d+|[a-zA-Z]+')
# x = re_object.findall(a)
# print(x)
# res = re.findall('\d+|[a-zA-Z]+',a)
# print(res)

# 将字符串序列化
# list_a = a.split()
# 移除筛选出来的东西
# for i in res:
#     list_a.remove(i)
#
# print(list_a)
# 拼接成字符串
# a = ' '.join(list_a)
# print(a)

###############################################

#正则匹配替换
# import re
# a = "张明 98分"
# res = re.sub(r'\d+','100',a)
# print(res)

############################################
# a = '你好'
# #编码成byte类型
# a = a.encode()
# print(a)

##############################################

# 在有空格的时候all()是True空格也是内容
# a = [1,23,4,5,6,' ']
# c = [1,23,4,5,6,'']
# # print(any(a))
# print(all(a))
# print(all(c))
# # 为什么all()时[1,23,4,5,6,' ']和[1,23,4,5,6,'']结果不一样

################################################

# #copy和deepcopy
# import copy
# #不可变类型
# #不论是copy还是deepcopy共享一个地址相当于赋值=，当数字改变地址相应改变
# a = 1
# c = copy.copy(a)
# d = copy.deepcopy(a)
# print(id(c))
# print(id(d))
# d = 2

#可变类型
#copy和deepcopy独立内存，两个操作内存地址不一样，当数值改变时地址并不会改变
#copy浅复制不能复制子对象，deepcopy可以复制子对象
# f = [1,2,3]
# f1 = copy.copy(f)
# f2 = copy.deepcopy(f)
#
# print(id(f1))
# f.append(3)
# print(id(f1))
# print(id(f2))

############################################

# foo = [-5,8,0,9,-4,-20,-2,8,2,-4]
# #key很重要
# #从小到大排序
# res1 = sorted(foo,key=lambda x:x)
# print(res1)

# #正数从小到大，负数从大到小
# res2 = sorted(foo,key=lambda x:(x<0,abs(x)))
# print(res2)

##############################################

# foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]
# #根据所提供key规则进行排序
# res1 = sorted(foo,key=lambda x:x['name'])
# print(res1)
# res2 = sorted(foo,key=lambda x:x['age'])
# print(res2)


######################################

# import re
# s = "info:xiaoZhang 33 shangdong"
#
# res = re.split(' |:',s)
# print(res)

#########################################

#递归求和1+2+3+...+10

# def get_sum(num):
#     if num:
#         num = num + get_sum(num-1)
#     return num
#
# result = get_sum(10)
# print(result)

#######################################
#json
# import json
# dict1 = {'a':1,'e':12}
# res1 = json.dumps(dict1)
# print(res1,type(res1))
#
# res2 = json.loads(res1)
# print(res2,type(res2))

#########################################

#python垃圾回收机制

#引用计数机制
#标记清除机制
#分代回收机制

##########################################