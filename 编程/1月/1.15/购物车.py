goods = ['Iphone: 5000','mac Pro: 12000','alex python: 81','Bike: 800','Starback latte: 31']
salary = input('请输入您的工资：')
print('------- 商品列表如下输入序号即可加入购物车 -------')
print('温馨提示：输入序号8即可退出程序！')
for i in goods:
    print(goods.index(i)+1,'. '+i)

shopping_car = []
while True:
    shopping_num = int(input('请输入要购买的商品序号：'))
    if shopping_num == 1:
        shopping_car.append(goods[shopping_num-1])
        continue
    elif shopping_num == 2:
        shopping_car.append(goods[shopping_num-1])
        continue
    elif shopping_num == 3:
        shopping_car.append(goods[shopping_num - 1])
        continue
    elif shopping_num == 4:
        shopping_car.append(goods[shopping_num - 1])
        continue
    elif shopping_num == 5:
        shopping_car.append(goods[shopping_num - 1])
        continue
    elif shopping_num == 8:
        break
    else:
        print('没有该商品请重新输入商品序号：')
        continue

print('您所购买的商品如下：')
for i in shopping_car:
    print(shopping_car.index(i),'.'+i)




