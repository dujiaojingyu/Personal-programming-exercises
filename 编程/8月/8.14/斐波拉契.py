__author__ = "Narwhale"

# #递归
# def fib(n):
#     """斐波拉契"""
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return fib(n-1)+fib(n-2)
#
#
# f = fib(50)
# print(f)


#
# #循环
# def fib(n):
#     """斐波拉契"""
#     a,b = 0,1
#     while n > 0:
#         a,b = b,a+b
#         n -= 1
#     return b
# f = fib(50)
# print(f)



# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        a, b = 1, 1
        while n > 2:
            a, b = b, a + b
            n -= 1
        return b

s = Solution()

print(s.Fibonacci(4))