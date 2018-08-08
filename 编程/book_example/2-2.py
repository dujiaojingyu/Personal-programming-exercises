import datetime

today = datetime.date.today()
month = int(input("请问你是在哪一个月份出生："))
day = int(input("请问你是出生日是几号："))
birthday = datetime.date(today.year, month, day)

if birthday < today:
  birthday = datetime.date(today.year+1, month, day)

diff = birthday - today
if diff.days == 0:
  print("不会吧！今天是你的生日，祝你生日快乐！")
else:
  print("哇！再过 " + str(diff.days) + " 天就是你的生日了！")