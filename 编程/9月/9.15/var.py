__author__ = "Narwhale"
import string

# def func(name):
#     return name.title()
#
# assert func("lilei")    #title
# assert func("hanmeimei")
# assert func("Hanmeimei")

# def func(name,callback=None):
#     if callback == None:
#         return name.title()
#     else:
#         return callback(name)
#
# def ff(name):
#     return name.lower()
# def f(name):
#     return name.upper()
#
#
# print(func("LILEI",callback=ff) == "lilei")
# assert func("lilei") == "Lilei"
# assert func("LILEI",callback=ff) == "lilei"
# assert func("lilei",callback=f)== "LILEI"


def getitem(*kargs):
    return kargs

l = getitem(5,3,4,5,6)
print(l)