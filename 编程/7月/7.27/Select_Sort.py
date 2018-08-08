__author__ = "Narwhale"

def select_sort(alist):
    """选择排序"""

    n = len(alist)
    #外循环
    for j in range(0,n-1):
        #内循环
        min_index = j
        for i in range(j+1,n):
            if alist[min_index] > alist[i]:
                min_index = i
        #将一轮循环之后最小的数交换出来
        alist[j],alist[min_index] = alist[min_index],alist[j]

li = [54,26,93,17,77,31,44,55,20]
select_sort(li)
print(li)

# for k in range(10,0,-1):
#     print("k",k,end=" ")