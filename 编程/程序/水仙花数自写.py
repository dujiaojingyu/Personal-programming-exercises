
i = 100

while i <= 999:
    g = (i//1)%10
    s = (i//10)%10
    b = (i//100)%10
    z = g**3 + s**3 + b**3
    if z == i:
        print(i)
    i +=1
    
