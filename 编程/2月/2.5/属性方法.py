__author__ = "Narwhale"


class Dog(object):

    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        print(" %s is eating" % self.name)
    @eat.setter
    def eat(self,food):
        print('set to %s'%food)

d = Dog("张三")
d.eat
d.eat = 'baizi'