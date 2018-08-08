
user,passwd = 'hsj','1234'

def auth(func):
    def wrapper(*args,**kwargs):
        username = input('Username:').strip()
        password = input('Password:').strip()

        if username == user and password == passwd:
            print('\033[32;1mUser has pass authentication\033[0m')
            func(*args,**kwargs)
        else:
            exit('\033[31;1mInvalid username or password\033[0m')
    return wrapper


def index():
    print('welcome to index psge')
@auth
def home():
    print('welcome to home page')
@auth
def bbs():
    print('welcome to bbs page')

index()
home()
bbs()