__author__ = "Narwhale"

class School(object):

    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self,stu_obj):
        print('为学员%s，办理注册手续！'% stu_obj.name )
        self.students.append(stu_obj)
    def hire(self,staff_obj):
        print('雇佣%s当老师。。。！'%staff_obj.name)
        self.staffs.append(staff_obj)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tall(self):
        pass



class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tall(self):
        print('''
        --------info  of %s -------
        Name:%s
        Age:%s
        Sex:%s
        salary:%s
        Course:%s
        '''%(
            self.name,
             self.name,
             self.age,
             self.sex,
             self.salary,
             self.course
            )

              )

    def teach(self):
        print('%s开始教%s了'%(self.name,self.course))


class student(SchoolMember):
    def __init__(self, name, age, sex, grade, stu_id):
        super(student, self).__init__(name, age, sex)
        self.grade = grade
        self.stu_id = stu_id

    def tall(self):
        print('''
        --------info  of %s -------
        Name:%s
        Age:%s
        Sex:%s
        Grade:%s
        Stu_id:%s
        ''' %
              (
            self.name,
            self.name,
            self.age,
            self.sex,
            self.grade,
            self.stu_id
              )

              )

    def pay_tuition(self,amount):
        print('%s 交学费%s元' % (self.name, amount))



school = School('市一中','广州')

t1 = Teacher('李四',25,'M',3000,'数学')
t2 = Teacher('张三',22,'M',3500,'化学')

s1 = student('晓明',18,'M','高一',1001)
s2 = student('小红',17,'F','高一',1002)

# t1.tall()
# t2.tall()
#
# s1.tall()
# s2.tall()

s1.pay_tuition(3500)

school.hire(t1)
school.enroll(s1)
print(school.students[0].name)
print(school.staffs[0].name)
school.staffs[0].teach()            #school.staffs相当于t1即t1.teach()