__author__ = "Narwhale"


def f(max):
    n,a,b = 0,0,1
    while max > n:
        print(b)
        a,b = b,a+b
        n+=1

f(6)