__author__ = "Narwhale"
string = input()
lenth = len(string)
num = 1
if string.upper() != string:
    num = 0
if string.upper() == string:
    # 条件一：检测AAA
    for i in range(lenth - 1):
        if string[i] == string[i + 1]:
            num = 0
            break
    #条件二：检测ABACADA
    for i in range(lenth - 3):
        print(string[i])
        x1 = string.find(string[i], i + 2)
        print('x1:',x1)
        if x1 == -1:
            continue
        else:
            #条件三：检测THETXH
            for j in range((i + 1), x1):
                print(string[j])
                x2 = string.find(string[j], (x1 + 1))
                print('x2:',x2)
                if x2 > 0:
                    num = 0
                    break

if num == 0:
    print('Dislikes')
else:
    print('Likes')









