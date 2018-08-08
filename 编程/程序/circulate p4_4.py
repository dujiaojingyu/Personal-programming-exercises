bingo = '小甲鱼是帅哥'
answer = input('请输入小甲鱼最想听的一句话：')
count = 3

while 0 < count <= 3:
    if answer == bingo:
        print('哎哟，帅哦~')
        print('您真是小甲鱼肚子里的蛔虫啊^_^')
        break

    print ("抱歉输入错误！还有" + str(count) + "次机会！加油！") 
    answer = input('重新输入正确答案:')
    count -= 1

    if count == 0:
        print("结束了！")


