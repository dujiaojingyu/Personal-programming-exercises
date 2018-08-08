
def gcd(x , y):
    if y == 0 :
        return x 
    else :
        return gcd(y, x%y) #注意return
    
 
x = int(input('请输入第一个数字：'))
 
y = int(input('请输入第二个数字：'))
a = gcd(x,y) 
print('%d 和 %d 的最大公约数为：' %(x,y) ,a)
