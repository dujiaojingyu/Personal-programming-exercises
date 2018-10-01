__author__ = "Narwhale"

# import copy
#
# a = 'a'
# b = copy.copy(a)
# print(b)


###################################

# def multipliers():
#     return [lambda x:i*x for i in range(4)]
# print([m(2) for m in multipliers()])
# a = [lambda x:i*x for i in range(4)]
# print(a)
# for i in a:
#     print(i(2))


###############################

#现有两个元组(('a'),('b')),(('c'),('d'))，请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]
# a = (('a'),('b'))
# b = (('c'),('d'))
#
# res = zip(a,b)
# # for i in res:
# #     print(i)
# res1 = lambda x,y:zip(x,y)
# dic =[{k:v} for k,v in res1(a,b)]
# print(dic)

#######################################

# v = dict.fromkeys(['k1','k2'],[])
# print(v)
# print(v['k1'])
# v['k1'].append(666)
# print(v)
# v['k1'].append(777)
# print(v)
# v['k1']=777
# print(v)

#print('\n'.join([' '.join(['%s*%s=%-2s' % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]))

#################################################
# class Parent(object):
# 	x = 1
# class Child1(Parent):
#     pass
# class Child2(Parent):
# 	pass
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)


#########################################

#gen的x在生成器内，生成器有自己的作用域。所以x会报错，但是用lambda就不会了。
#
# class A(object):
#     x = 1
#     gen = (lambda x:x for _ in range(10))
#
#
# a = A()
# print(a.gen)