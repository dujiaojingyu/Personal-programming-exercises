__author__ = "Narwhale"

a = [1,2,3,4,5,6,7,8,9,10]
def func(x):
    return x%2 == 1

res = filter(func,a)

res = [i for i in res]
print(res)