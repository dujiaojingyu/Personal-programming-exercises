f = open("haproxy","r",encoding="gbk")
f_new = open("haproxy_new","w",encoding="gbk")
#将文件内容转换为一个列表，并定义一个变量。
b = f.readlines()
#定义三个选项：
option = ("1、请输入搜索的地址：","2、请输入增加的内容：","3、请输入删除的内容：")
#打印三个选项：
for i in option:
    print(i)
choice = input("请选择操作方式：序列号>>>")
#如果选择1，则进入查找选项。
if choice == "1" :
    data = input("请输入搜索地址：")
    #利用字符串拼接，定义一个变量，-----backend所在的行。
    address = "backend %s\n"%data
    if address in b:
        #利用列表的下标来定位位置，然后通过下标打印内容。
        index_add = b.index(address)
        print(b[index_add],b[index_add+1])
    if address not in b:
        print("您查找的内容不存在")
#如果选择2，则进入增加内容选项：
if choice =="2":
    data = input("输入增加内容：")
    data_eval = eval(data)
    #通过列表计数器来判断输入的内容是否在列表中存在，如果计数器为0则不存在，如果计数器不为0则存在。
    #不存在则添加，存在则不添加。
    f_find = b.count("backend %s\n"%data_eval["backend"])
    #如果backend后的内容在文件中不能找到则新增。
    if f_find == 0:
        for line in b:
            f_new.write(line)
       #  for f_line2 in f:
       # #将输入的内容通过字符串拼接的形式写入文件中
        f_new.write("\nbackend  ")
        f_new.write(data_eval["backend"])
        f_new.write("\n        server %s weight %s maxconn %s"\
                    %(data_eval["record"]["server"],data_eval["record"]["weight"]\
                    ,data_eval["record"]["maxconn"]))
    #如果backend后的内容在文件中能找到则不执行任何操作。
    if f_find != 0:
        print("您添加的内容已经存在")
#如果选择3，则进入删除内容选项：
if choice == "3":
    data = input("输入删除内容：")
    data_eval = eval(data)
    #通过列表计数器来判断输入的内容是否在列表中存在，如果计数器为0则不存在，如果计数器不为0则存在。
    #不存在则添加，存在则不添加。
    f_find = b.count("backend %s\n"%data_eval["backend"])
    #如果backend后的内容在文件中不能找到则新增。
    if f_find != 0:
            b_index=b.index("backend www.oldboy.org\n")
            b.pop(b_index)
            b.pop(b_index)
            for line in b:
                f_new.write(line)
    #如果backend后的内容在文件中不能找到则不执行任何操作。
    if f_find == 0:
        print("您输入的内容文件中不存在")
f.close()
f_new.close()