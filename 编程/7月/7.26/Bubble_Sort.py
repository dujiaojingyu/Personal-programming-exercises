__author__ = "Narwhale"



def bubble_sort(alist):
    """冒泡排序"""

    n = len(alist)
    for j in range(0,n-1):
        count = 0
        for i in range(0,n-1-j):
            #i的取值范围[0,n-2]
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if 0 == count:
            return

#冒泡排序最有时间复杂度为O(n),最差时间复杂度为O(n^2)

li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)
