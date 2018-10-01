__author__ = "Narwhale"

def fib(n):
    a,b = 0,1
    while n >= 0:
        print(b)
        a,b = b,a+b
        n -= 1



fib(100)
