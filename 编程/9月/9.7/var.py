__author__ = "Narwhale"

class A:
    def func(self):
        print("Hi")
def monkey(self):
    print("Hi, monkey")

A().func()

A.func = monkey

A().func()


#常用linux命令
#ls cd cp mv more mkdir touch  tree rm pwd clear