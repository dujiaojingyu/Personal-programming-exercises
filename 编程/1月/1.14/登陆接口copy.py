# 作业：编写登陆接口
# 输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后锁定

user = {'hepd':123456, 'hhhd':654321}       # 字典

name = input('用户名: ')

comm = 1
while name in user:
    password = int(input('密码: '))
    if comm < 3:
        if password == user[name]:
            print ('登录成功！欢迎')
            break
        else:
            comm += 1
            print ('密码错误！您还有%d次尝试机会，请重新输入密码' % (4 - comm))

    else:
        print ("尝试过多，账号已锁定！")
        break
else:
    print ('新用户名')
    password = int(input('密码: '))
    user[name] = password
    print (user)