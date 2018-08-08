a = int(input("输入数字a:"))
n = int(input("输入层数n:"))
sum = 0
print('s = ',end = '')
for i in range(1,n):
    g1 = str(a)*i  #转换成字符
    x = int(g1)    #转换成整数
    sum += x
    print(g1,"+ ",end='')

    if i == (n-1): #求最后一个数字
        g2 = g1+str(a)
        x1 = int(g2)
        sum += x1
        print(g2)
print('s = ',sum)


