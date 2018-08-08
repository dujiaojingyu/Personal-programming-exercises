# _*_ coding: utf-8 _*_

import random

game_count = 0
all_counts = []
while True:
  game_count += 1 
  guess_count = 0
  answer = random.randint(0,99)
  while True:
    guess = int(input("请猜一个数字(0-99)："))
    guess_count += 1
    if guess == answer:
      print("恭禧你，猜中了")
      print("你总共猜了" + str(guess_count) + "次")
      all_counts.append(guess_count)
      break;
    elif guess > answer:
      print("你猜的数字太大了")
    else:
      print("你猜的数字太小了")
  onemore = input("还要再玩一次吗(Y/N)？")
  if onemore != 'Y' and onemore != 'y':
    print("欢迎下次再来玩！")
    print("您的成绩如下：")
    print(all_counts)
    print("平均猜中次数" + str(sum(all_counts)/float(len(all_counts))))
    break;