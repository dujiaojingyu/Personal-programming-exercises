

boy = []
girl = []
count = 1
f = open("record2.txt")

for each_line in f:
    if each_line[:6] != "======": #注意"="要够6个
        (role,speaking) = each_line.split(':',1)
        if role == "小甲鱼":
            boy.append(speaking)
        if role == "小客服":
            girl.append(speaking)
    else:
        file_name_boy = "boy_" + str(count) + ".txt"
        file_name_girl = "girl_" + str(count) + ".txt"
        
        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl,'w')
        
        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()   #非常注意文件要关闭！要关闭！要关闭！
        girl_file.close()
        
        boy = []
        girl = []
        count += 1
        
file_name_boy = "boy_" + str(count) + ".txt"
file_name_girl = "girl_" + str(count) + ".txt"
        
boy_file = open(file_name_boy,'w')
girl_file = open(file_name_girl,'w')
        
boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()   #非常注意文件要关闭！要关闭！要关闭！
girl_file.close()
        
f.close()
