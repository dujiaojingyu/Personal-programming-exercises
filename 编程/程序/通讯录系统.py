
print("|--- 欢迎进入通讯录程序 ---|")
print("|--- 1：查询联系人资料  ---|")
print("|--- 2：插入新的联系人  ---|")
print("|--- 3：删除已有联系人  ---|")
print("|--- 4：退出通讯录程序  ---|")

contacts = {}

while True:
    
    flag = int(input("请输入相关指令代码："))

    if flag ==1:
        name = input("请输入联系人名字：")

        if name in contacts:
            print(name,":",contacts[name])
        else:
            print("通讯录中不存在此联系人！")

    elif flag == 2:
        name = str(input("请输入联系人名字："))

        if name in contacts:
            print("您输入的名字已存在通讯-->> " , name,":",contacts[name])
            choose = str(input("是否修改用户资料（YES/NO）:"))
            YES = 'YES'
            NO = 'NO'

            if choose == 'YES':
                phone = input("请输入用户联系电话：")
                contacts[name] = phone
                   
            elif choose == 'NO':
                continue
        else:
            phone = input("请输入用户联系电话：")
            contacts[name] = phone

    elif flag == 3:
        name =input("请输入要删除的联系人名字：")
        
        if name not in contacts:
            print("通讯录不存在该联系人!")
            
        else:
            contacts.pop(name)

    elif flag == 4:
        break

    else:
        print("指令代码错误请输入1-4")
print("|--- 感谢使用通讯录 ---|")
                
                 

