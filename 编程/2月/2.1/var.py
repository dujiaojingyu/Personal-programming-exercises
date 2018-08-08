__author__ = "Narwhale"
class Person:
    n = 123  #类变量

    def __init__(self,name,ability):
        #构造函数

        self.name = name     #实例化变量（静态属性） ，作用域为实例化本身
        self.ability = ability

    def eat(self):              # 类方法 功能（动态属性）
        print('I will eat something !  ')

    def run(self):
        print('I will runing !')

    def sleep(self):
        print('I will sleep !')

    def doing(self):
        print('I am %s'% self.ability)

r1 = Person('张三','dancing')

r1.sleep()
r1.run()
r1.eat()
r1.doing()
print(r1.n)