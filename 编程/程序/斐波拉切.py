def fun(n):
    if n < 0:
        print("输入错误！请输入大于0的数！")
    elif n == 1 or n == 2 :
        return 1
    else:
        return fun(n-1) + fun(n-2)


result = fun(10)
print(result)