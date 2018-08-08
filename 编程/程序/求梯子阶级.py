
x = 7
i = 1
flag = 0

while i <= 100:
    
    if (x % 2 == 1)and(x % 3 == 2)and(x % 5 == 4)and(x % 6 == 5)and(x % 6 == 5):
        flag = 1
        
    else:
        x = 7*(i+1)
    i += 1 #循环最重要的是条件要明确！！！！！！！
        
if flag ==1:
    print("阶级数是：",x)
else:
    print("不在程序限定范围内！")
