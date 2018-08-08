__author__ = "Narwhale"

class User(object):
    def __init__(self,first_name,last_name,username,Email,location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.Email = Email
        self.location = location

    def describe_user(self):
        '''打印用户详细信息'''
        print('\n',self.first_name + ' ' + self.last_name)
        print('    Username: ',self.username)
        print('    Email: ',self.Email)
        print('    Location: ',self.location)

    def green_user(self):
        '''表达问候'''
        print('Welcome back',self.username+'!')

# A = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# A.describe_user()
# A.green_user()

class Admin(User):
    '''管理员类'''
    def __init__(self,first_name,last_name,username,Email,location):
        super(Admin,self).__init__(first_name,last_name,username,Email,location)
        self.privileges = []
    def show_privileges(self):
        '''打印管理员权限'''
        print("\nPrivileges:")
        for i in self.privileges:
            print('   -',i.title())

C = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
C.describe_user()
C.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
C.show_privileges()
