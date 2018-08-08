__author__ = "Narwhale"
# user_name = 'hsj'
# user_passwd = 1111
import os,json
from core import db_handle

def acc_login():
    '''
    登录函数，错误次数限制为3次，客户信息保存在Mysql或者文件里，文件存放在db目录下的accounts
    :return:
    '''
    count = 0
    while True:
        user_input_name = input('Name:').strip()
        db_data = db_handle.file_db_handle(user_input_name)
        user_name = db_data['id']
        user_passwd = db_data['password']
        status = db_data['status']
        while count < 3:
            if str(user_input_name) == str(user_name):
                if status == 0:      #status为1时锁开，0时锁关
                    user_input_passwd = input('Passwd:').strip()
                    if str(user_input_passwd) == str(user_passwd):
                        print('登录成功！')
                        return db_data
                    else:
                        count += 1
                        if count < 3:
                            print('密码错误请重新输入！')
                        else:
                            print('密码错误3次！帐号已锁定,请联系服务人员！')
                            return    #这里返回status给hsj.json
                else:
                    print('帐号已锁定，请联系服务人员！')
                    break
            else:
                print('此用户名不存在!')
                break



def acc_enroll():
    '''
    注册函数
    :return:
    '''
    checking = False
    data = {"balance": 0,
            "expire_date": "2021-01-01",                #可加入时间模块
            "enroll_date": "2016-01-02",
            "credit": 15000,
            "id":None,
            "status": 0,
            "pay_day": 22,
            "password": None}
    while not checking:
        New_user_name = input('New_user_name:').strip()
        file_path = db_handle.file_path()
        #print('%s\%s.json'%(file_path,user_name))
        checking = os.path.isfile('%s\%s.json'%(file_path,New_user_name))      #可以写成一个函数检查文件是否存在

        if not checking:
            New_user_passwd = input('New_user_passwd:')
            data['id'] = New_user_name
            data['password'] = New_user_passwd
            with open('%s\%s.json'%(file_path,New_user_name),'w') as f:
                json.dump(data,f)
            f.close()
            print('注册成功！请登录试试吧！')
            return acc_login()
        else:
            print('用户名已经存在！')             #加入身份证号可以同名的人注册，且文件名用身证号
            checking = False


