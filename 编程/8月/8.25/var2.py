__author__ = "Narwhale"
#列表合并
# a = [1,3,5,7,9]
# b = [2,4,6,8,10]
#
# a.extend(b)
# a.sort()
# print(a)

###############################
#自定义异常

# def fun():
#     try:
#         for i in range(5):
#             if i > 2:
#                 raise Exception('数字大于2了')
#     except Exception as ret:
#         print(ret)
#
# fun()

########################################
#(.*)和(*?)的区别
#(.*)为贪婪匹配，(.*?)为非贪婪匹配

# import re
# s = '<a>哈哈</a><a>啊啊</a>'
# reobject1 = re.compile("<a>(.*)</a>")
# reobject2 = re.compile("<a>(.*?)</a>")
# res1 = reobject1.findall(s)
# res2 = reobject2.findall(s)
# print(res1)
# print(res2)

#############################
#列表的解耦
# a = [[1,2],[3,4],[5,6]]
# x = [j for i in a for j in i ]
# print(x)

#############################
# x = 'abc'
# y = 'def'
# z = ['d','e','f']
#
# m = x.join(y)
# n = x.join(z)
# print(m)
# print(n)


#############################

# try:
#     num = 100
#     print(num)
# except NameError as erroMsg:
#     print('产生错误了：%s'%erroMsg)
# else:
#     print('没有捕获到异常执行此语句')
#
# try:
#     num = 100
#     print(num)
# except NameError as erroMsg:
#     print('产生错误了：%s' % erroMsg)
# finally:
#     print('不管有没有捕获到异常都执行此语句')
#


##########################################
#保留两位小数

# a = '%.03f'%1.3335
# print(a,type(a))
# b = round(float(a),1)
# print(b,type(b))
# c = round(float(a),2)
# print(c,type(c))


#############################################

import re
a = '123214abfcdefgadcafc'
# res = re.compile('[0-9]')

r = re.findall('\d+|a\w+c',a)
print(r)