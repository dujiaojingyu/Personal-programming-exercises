
def count(*param):
    length = len(param)
    for i in range(length):
        letter = 0
        digital = 0
        space = 0
        other = 0

        for each in param[i]:
            if each.isdigit() == True:
                digital += 1
            elif each.isalpha() == True:
                letter += 1
            elif each.isspace() == True:
                space +=1
            else:
                other += 1
        print("字母：%d，数字：%d,空格：%d，其他字符：%d"%(letter,digital,space,other))
count('I love fichc','I love you!')
