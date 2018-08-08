__author__ = "Narwhale"

# for i in range(1,21):
#     print(i)

#---------一百万---------------

ls = [i for i in range(1,1000001)]

# for v in ls:
#     print(v)

#-----------逻辑 计算--------------
# print(max(ls))
# print(min(ls))
# print(sum(ls))

#---------奇数-----------------

# for i in range(1,20,2):
#     print(i)

#----------3的倍数--------------

# ls2 = [r for r in range(3,30) if r%3==0]
#
# for i in ls2:
#     print(i)

#-----------立方------------------

cube = [str(r) +'**3' for r in range(1,11)]

for i in cube:
    print(i)