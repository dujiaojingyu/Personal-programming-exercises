__author__ = "Narwhale"
class Dog(object):

    def __init__(self,name):
        self.name = name

    @staticmethod
    def eat():
        print(" is eating")
        return 'eating'



d = Dog("张三")
d.eat()