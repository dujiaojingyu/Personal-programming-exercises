__author__ = "Narwhale"
#
# l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
# l2 = {}.fromkeys(l1).keys()
#
# print(l2)
#
# l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
# l2 = list(set(l1))
# print(l1.index)
# l2.sort(key=l1.index)
# print(l2)


items = [('name', 'earth'), ('port', '80')]
dict2 = dict(items)
dict1 = dict((['name', 'earth'], ['port', '80']))

print(dict1)
print(dict2)