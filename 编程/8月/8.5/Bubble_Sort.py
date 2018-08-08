__author__ = "Narwhale"

def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    #控制循环多少遍，以及多少数字是不用究进入循环的
    for j in range(0,n-1):
        count = 0
        #控制从头开始前一个与后一个比较
        for i in range(0,n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if count == 0:
            break

li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)