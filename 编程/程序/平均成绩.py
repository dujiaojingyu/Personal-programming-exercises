numbers = []
while True:
    x = input("请输入一个整数：")
    try:
        numbers.append(int(x))
    except:
        print("不是整数！")
    while True:
        flag = input("继续输入吗？（yes/no）")
        if flag.lower() not in ("yes","no"):
            print("只能输入yes或no")
        else:
            break
    if flag.lower() == 'no':
        break
print(sum(numbers)/len(numbers))