a = int(input("输入第一个数："))
b = int(input("输入第二个数："))
c = int(input("输入第三个数："))

if a < b :
    small = a
    if small > c :
        small = c
elif b < c :
    small = b
else:
    small = c
print(small)


