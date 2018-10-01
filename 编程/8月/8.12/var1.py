__author__ = "Narwhale"

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        print('--->',hasattr(cls,"_instance"))
        if not hasattr(cls,"_instance"):
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
            print(cls._instance)
        return cls._instance

class Foo(Singleton):
    pass

foo1 = Foo()
foo2 = Foo()

print(foo1 is foo2)