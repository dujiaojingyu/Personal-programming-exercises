def discounts(price,rate):
    final_price = price * rate
    return final_price

old_price = int(input("请输入价格:"))
rate = float(input("请输入折扣："))
new_price = discounts(old_price,rate)
print("最后的价格是:",new_price)
