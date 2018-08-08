
def myfun(*prag,base = 3):
    result = 0

    for each in prag:
        result += each

    result = result * base

    
    print("结果为：",result)
