__author__ = "Narwhale"

def select_sort(alist):
    """选择排序"""
    n = len(alist)
    #外层循环
    for j in range(0,n-1):
        #内层循环
        min_index = j
        for i in range(j+1,n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index],alist[j]


#j=0  i=(1+0,n)
#j=1  i=(1+1,n)
#j=2  i=(1+3,n)
#j=3  i=(1+4,n)


li = [54,26,93,17,77,31,44,55,20]
select_sort(li)
print(li)
