__author__ = "Narwhale"


def fibonacci(n):
    a,b = 0,1
    while n >= 0:
        print(b,end=' ')
        a,b = b,a+b
        n -= 1

def fibonacci1(n):
    a,b = 0,1
    while n > 0:
        a,b = b,a+b
        n -= 1
    return b




fibonacci(4)
print(fibonacci1(4))

