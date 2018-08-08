__author__ = "Narwhale"

def bubble_sort(alist):
    """冒泡排序"""

    n = len(alist)
    #外循环
    for j in range(0,n-1):
        #内层循环
        count = 0
        for i in range(0,n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if 0 == count:
            return


#j=0      i=(0,n-1)
#j=1      i=(0,n-2)
li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)


