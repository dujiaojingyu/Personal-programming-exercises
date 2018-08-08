__author__ = "Narwhale"


def insertion_sort(alist):
    """插入排序"""
    #外层循环
    #控制未排序区的取值
    n = len(alist)
    for j in range(1,n):
        #内层循环
        #控制排序区的比较
        for i in range(j,0,-1):
            if alist[i-1] > alist[i]:
                alist[i-1],alist[i] = alist[i],alist[i-1]

li = [54,26,93,17,77,31,44,55,20]
insertion_sort(li)
print(li)
