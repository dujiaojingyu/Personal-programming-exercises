# __author__ = "Narwhale"
#
# def binary_search(alist,item):
#     """二分查找"""
#     n = len(alist)
#     low = 0
#     high = n - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if alist[mid] == item:
#             return mid
#         elif alist[mid] > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return
#
#
# alist = [1,2,3,4,5,6,7,8,9,45,47,56,87,89]
#
# b = binary_search(alist,99)
# print(b)


##############################################

#生成字典
import random

def random_list(n):
    result = []

    ids = list(range(1001,1001+n))
    a1 = ('李','黄','张','陈','展','朱')
    a2 = ('世','始','好','化','桦','莉')
    a3 = ('杰','超','俊','宝','华','成')
    for i in range(n):
        id = ids[i]
        age = random.randint(18,60)
        name = random.choice(a1)+random.choice(a2)+random.choice(a3)
        dict1 = dict(id=id,age=age,name=name)
        result.append(dict1)
    return result

r = random_list(100)
print(r)

def binary_search(alist,item):
    """二分查找"""
    n = len(alist)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if alist[mid]['id'] == item:
            return mid,alist[mid]['id'],alist[mid]['age'],alist[mid]['name']
        elif alist[mid]['id'] > item:
            high = mid - 1
        else:
            low = mid + 1
    return




b = binary_search(r,1001)
print(b)