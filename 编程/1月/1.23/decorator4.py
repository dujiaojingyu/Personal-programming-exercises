
user,passwd = 'hsj','1234'

def auth(auth_type):
    print('auth func:',auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print('wrapper:',*args, **kwargs)
            if auth_type == 'local':
                username = input('Username:').strip()
                password = input('Password:').strip()

                if username == user and password == passwd:
                    print('\033[32;1mUser has pass authentication\033[0m')
                    return func(*args, **kwargs)  # from home         #函数wrapper的返回值
                else:
                    exit('\033[31;1mInvalid username or password\033[0m')
            elif auth_type =='ldap':
                print('ldappppppppp')
        return wrapper
    return outer_wrapper

def index():
    print('welcome to index psge')
@auth(auth_type='local')      # '''加了括号相当于运行了outer_wraper所以会执行里面内容'''        # home = auth(home)
def home():
    print('welcome to home page')
    return 'from home'         #这里有返回值在装饰器里也应该有个返回值不然是print（）不出来的
@auth(auth_type='ldap')
def bbs():
    print('welcome to bbs page')

index()
print(home())
bbs()