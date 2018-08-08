__author__ = "Narwhale"

def func(self):
    print('hello %s'%self.name)

def __init__(self,name,age):
    self.name = name
    self.age = age

Foo = type('Foo',(object,),{'func':func,'__init__':__init__})

f = Foo('limin',23)
f.func()
