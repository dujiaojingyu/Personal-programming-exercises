
date = {}

def new_user():
    name = input("请输入用户名字：")
    while True:

        if name in date:
            name = input("此用户名已经被使用，请重新输入：")

        else:
            password = input("请输入密码：")
            date[name] = password
            print("注册成功请登录试试！")
            break

def entry():
    name = input("请输入用户名字：")

    while True:

        if name not in date:
            name = input("您输入的用户名不存在，请重新输入：")

        else:
             password = input("请输入密码：")
             
             while True:
                 if password not in date.values():
                     password = input("密码错误，请重新输入密码：")
                 else:
                     print( "欢迎进入xxxx系统，点击右上角的x结束程序！")
                     break
             break            
        

def menu():
    print("|--- 新建用户：N/n ---|")
    print("|--- 登录账户：E/e ---|")
    print("|--- 推出程序：Q/q ---|")

    while True:
        chosen = False
        choice = input("请输入指令代码:")
        while not chosen:
            if choice not in 'NnEeQq':
                 choice = input("您输入的代码错误，请重新输入指令代码:")
            else:
                chosen = True



        if choice =='Q' or choice == 'q':
            break
        if choice == 'N' or choice == 'n':
            new_user()
        if choice == 'E' or choice == 'e':
            entry()
    


menu()


