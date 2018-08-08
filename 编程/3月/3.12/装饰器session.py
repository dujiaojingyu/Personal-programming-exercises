__author__ = "Narwhale"


user_list = [
    {'name':'hsj','passwd':'1111'},
    {'name':'hsj1','passwd':'1112'},
    {'name':'hsj2','passwd':'1113'},
    {'name':'hsj3','passwd':'1114'},
]

current_dict = {'username':None,'login':False }

def auth_fun(fun):
    def wrapper(*args,**kwargs):
        if current_dict['username'] and current_dict['login']:
            res = fun(*args,**kwargs)
            return res
        username = input('用户名：').strip()
        passwd = input('密码：').strip()
        for row in user_list:
            if username == row['name'] and passwd == row['passwd']:
                current_dict['username'] = username
                current_dict['login'] = True
                res = fun(*args,**kwargs)
                return res
        else:
            print('用户名或者密码错误')
    return wrapper




@auth_fun
def index(name):
    print('%s欢迎来到京东主页'%(name))
@auth_fun
def home(name):
    print('%s欢迎回家'%name)

@auth_fun
def shopping_car(name):
    print('%s购物车里有[%s，%s]'%(name,'牛奶','花生'))


index('aj')
home('aj')
shopping_car('aj')
