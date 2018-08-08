goods = [('Iphone',50000),('mac Pro',12000),('alex python',81),('Bike',800),('Starback latte',31)]
print('------- 商品列表如下输入序号即可加入购物车 -------')
print('温馨提示：输入q即可退出程序！')
salary = input('请输入您的工资：')
shopping_list = []
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(goods):
            print('%s.%s'% (index,item))

        user_choice = input('请输入需要购买的商品序号：')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(goods) and user_choice >= 0:
                p_item = goods[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(goods[user_choice])
                    salary = salary - p_item[1]
                    print("%s已经添加到购物车中，您的余额还剩%s元！"% (p_item,salary))
                else:
                    print('您的余额还剩%s不够了！'% salary)
            else:
                print('错误选项！商品不存在，请重新选择！')
        elif user_choice == 'q'and 'Q':
            print('------购物车东西如下---------')
            for i in shopping_list:
                print(i)
            print('您的余额还剩%s...' % salary)
            break
        else:
            print('错误选项！')
