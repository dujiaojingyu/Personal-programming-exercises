__author__ = "Narwhale"

# ls = [1,2,3,4,5月,6,7,8,9]
# print(ls[-9:])
# s = 'The first three items in the list are:'
# print(s)
# print(s[:3])


my_pizza = ['番茄浆','火腿','牛肉']

friends_pizza = my_pizza[:]

my_pizza.append('茄子')
friends_pizza.append('猪肉')

print('My favorite pizzas are:')
for i in my_pizza:
    print(i)

print("My friend\'s favorite pizzas are:")
for t in friends_pizza:
    print(t)

# print(my_pizza)
# print(friends_pizza)
