__author__ = "Narwhale"
user_list = [
    {'name':'hsj','passwd':'1111'},
    {'name':'hsj1','passwd':'1112'},
    {'name':'hsj2','passwd':'1113'},
    {'name':'hsj3','passwd':'1114'},
]
current_dic = {'username':None,'login':False}

def auth_fun(fun):
    def wrapper(*args,**kwargs):
        if current_dic['username'] and current_dic['login']:
            res = fun(*args,**kwargs)
            return res
        username = input('用户名：').strip()
        passwd = input('密码：').strip()
        for i in user_list:
            if username == i['name'] and passwd ==i['passwd']:
                current_dic['username'] = username
                current_dic['login'] = True
                print('登陆成功')
                res = fun(*args,**kwargs)
                return res
        else:
            print('用户名或密码错误')
    return wrapper



@auth_fun
def index(name):
    print('%s欢迎来到京东主页'%name)
@auth_fun
def home(name):
    print('%s欢迎回家'%name)
@auth_fun
def shopping_car(name):
    print('%s的购物车里有[%s,%s]'%(name,'杯子','茶壶'))


index('sj')
home('sj')
shopping_car('sj')