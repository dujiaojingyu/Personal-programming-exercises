import math
def isPrime(n):
    #判断是否是素数
    m = int(math.sqrt(n)) + 1
    for i in range(2,m):
        if n % i == 0:
            return False
    return True

def demo(n):
    #分解正偶数
    if (n % 2 == 0) and isinstance(n,int) and (n > 0): #判断n是否符合条件
        for j in range(3,int(n/2)+1):
            if (j % 2 == 1) and isPrime(j) and isPrime(n-j):
                print(j , "+" , n-j , "=" , n)

demo(60)