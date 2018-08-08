
count = 3
password = "FishC.com"

while count:
    passwd = input("请输入密码：")
    if passwd == password:
        print("密码正确")
        break
    elif '*' in passwd:
        print("密码不能包含'*'请重新输入！您还有",count ,"次机会！",end = '')
        continue

    else:
        print('密码输入错误！您还有', count-1, '次机会！', end=' ')
        
    count -=1
