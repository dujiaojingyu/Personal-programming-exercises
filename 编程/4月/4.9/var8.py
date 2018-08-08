__author__ = "Narwhale"

# sandwich_orders = ['奶油味','草莓味','莎拉味']
# finshed_sandwich = []
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print('I make your %s sandwich'%(sandwich))
#     finshed_sandwich.append(sandwich)
# print('\nfinshed_sandwich:')
# for i in finshed_sandwich:
#     print(i)

#-----------------------------------------

sandwich_orders = ['奶油味','pastrami','草莓味','pastrami','莎拉味','pastrami','pastrami','pastrami']
print('Pastrami has all been sold out!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print(sandwich_orders)