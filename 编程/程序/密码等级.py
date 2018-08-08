
symbols = r"~!@#$%^&*()_=-/,.?<>;:[]{}|\）"
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

password = input("请输入需要检查的密码：")
length = len(password)

while password.isspace() or length ==0:
    password = input("密码不能为空（或空格），请重新输入要检查的密码：")


if length <= 8:
    flag_len = 1
elif 8 < length < 16:
    flag_len = 2
else:
    flag_len = 3


flag_con = 0

for each in password:
    if each in chars:
        flag_con += 1
        break

for each in password:
    if each in symbols:
        flag_con += 1
        break


for each in password:
    if each in nums:
        flag_con += 1
        break

while True:
    
    if flag_len == 1 or flag_con == 1 :
        print("密码安全等级低")
        break
    
    if flag_len == 2 or flag_con == 2:
    
        
        print("密码安全等级中")
        break
    

    else:
        print("密码安全等级高")
        break
    

        
