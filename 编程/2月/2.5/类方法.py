__author__ = "Narwhale"


class Dog(object):
    name = "类变量"

    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(self):
        print("%s is eating" % self.name)


d = Dog("张三")
d.eat()

