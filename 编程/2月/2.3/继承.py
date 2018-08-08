__author__ = "Narwhale"
#父类1
class Person(object):         #新式写法

    def __init__(self,name,age):
        #构造函数
        self.name = name           #实例化变量（静态属性） ，作用域为实例化本身
        self.age = age
        self.friends = []

    def eat(self):                  # 类方法 功能（动态属性）
        print('%s will eat something ! '%self.name)

    def run(self):
        print('%s will runing !'%self.name)

    def sleep(self):
        print('%s will sleep !'%self.name)

#父类2
class Relation(object):
    def make_friends(self,obj):
        print('%s make friend with %s'% (self.name,obj.name))
        self.friends.append(obj)       #这里传的参数是obj，在这例题里 obj既是 w1


#子类
class Man(Person,Relation):                      #多继承
    def __init__(self,name,age,money):           #重写构造函数
        #Person.__init__(self,name,age,money)     #经典写法
        super(Man,self).__init__(name,age)        #新式写法，建议用这种写法
        self.money = money

    def piao(self):
        print('%s is piaoing .......'% self.name)


#子类
class Woman(Person,Relation):                 #多继承
    def piao(self):
        print('%s is piaoing .......'% self.name)

m1 = Man('张三',20,10)

w1 = Woman('lili',21)

m1.make_friends(w1)
print(m1.friends[0].name)
print(m1.friends[0].age)

# m1.piao()
# m1.eat()
# m1.run()
# m1.sleep()



