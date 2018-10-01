__author__ = "Narwhale"

class Single_instance(object):
    """单例模式"""
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

s = Single_instance()
a = Single_instance()
print(id(s),id(a))