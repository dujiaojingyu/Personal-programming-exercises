age = int(input("你的年龄是："))
if age >= 18:
  print("恭喜！你成年了。")
else:
  diff = str(18 - age)
  print("要年满18岁才成年，你还差 " + diff + " 岁")
