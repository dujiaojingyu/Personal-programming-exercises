__author__ = "Narwhale"

class Employee(object):
    '''关于员工信息的类'''
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self,amount=5000):
        '''自动增长5000美元'''
        self.salary += amount
        return self.salary