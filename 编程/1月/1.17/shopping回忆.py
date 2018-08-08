commodity = [('Iphone',50000),('mac Pro',12000),('alex python',81),('Bike',800),('Starback latte',31)]
print('------- 商品列表如下输入序号即可加入购物车 -------')
print('温馨提示：输入q即可退出程序！')
salary = input('请输入您的工资：')
shopping_list = []
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, goods in enumerate(commodity):
            print(index, '.', goods)
        user_choice = input('请输入你要购买的商品的序号：')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(commodity) and user_choice >=0:
                item = commodity[user_choice]
                if salary > item[1]:
                    shopping_list.append(item)
                    salary = salary  - item[1]
                    print('您购买的商品%s,已经加入到购物车，您的余额还剩%s啦！' % (item[0],salary))

                else:
                    print('您的余额还有%s，不够买了！'%salary)
            else:
                print('没有该商品请重新输入！')
        elif user_choice == 'q' and 'Q':
            print('-----您购买的商品如下-----')
            for i in shopping_list:
                print(i)
            print('您的余额还剩%s  ！' %salary)
            exit()
        else:
            print('错误选项！')

else:
    print('输入有误！')