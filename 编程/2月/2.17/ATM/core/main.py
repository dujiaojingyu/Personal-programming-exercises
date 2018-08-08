__author__ = "Narwhale"

from core import auth

# user_data = {
#     'account_id':None,
#     'is_authenticated':False,
#     'account_data':None
# }
def interactive():
    '''
    此函数为与客户的交互模块，打印选项供客户选择。
    :return:
    '''
    print('你好！')



def run():
    '''
    这个函数主要执行运登录程序以及执行与客户的交互
    :return:
    '''
    select = '''
--------选项---------
      1.登录
      2.注册
    '''
    print(select)
    user_select = input('请输入你的选择：')
    selsct_dict = {'1':'auth.acc_login()','2':'auth.acc_enroll()'}
    if user_select in selsct_dict:
        acc_data = eval(selsct_dict[user_select])
        if acc_data:
            interactive()
    else:
        print('超出选项')
