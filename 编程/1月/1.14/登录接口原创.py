user = 'hsj'
password = 1234
count = 0
while count < 3:
    users = input('输入用户名：')
    pd = int(input('请输入密码'))
    if users == user and pd == password:
        print("Welcome user {user} login...".format(user=users))
        break
    else:
        count += 1
        if count ==3:
            print('Sorry to enter 3 error messages, the user has been locked!')
            break
        else:
            print("you input username error or password error ! Please input it!")
            continue


