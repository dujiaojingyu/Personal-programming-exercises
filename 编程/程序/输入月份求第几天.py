
year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
day = int(input("请输入日:"))

months = (0,31,59,90,120,151,181,212,244,273,304,334)
if 0 < month <=12:
    sum = months[month - 1]
else:
    print("输入错误！")

sum += day
flag = 0

if (year %400 == 0) or (year % 100 == 0 and year % 4 ==0):
    flag = 1
    if (flag == 1) and (month > 2 ):
        sum += 1
        print(sum)

