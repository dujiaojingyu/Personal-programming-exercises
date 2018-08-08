__author__ = "Narwhale"

# def insert_sort(alist):
#     """插入排序"""
#     n = len(alist)
#     #外层循环控制取数来比较
#     for j in range(1,n):
#         i=j
#         #内城循环控制比较过程
#         for i in range(i,0,-1):
#             if alist[i] < alist[i-1]:
#                 alist[i],alist[i-1] = alist[i-1],alist[i]

def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for i in range(1,n):
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                i -= 1
            #加了else之后优化了时间复杂度为O(n),未优化前为O(n^2)
            else:
                break


li = [54,26,93,17,77,31,44,55,20]
insert_sort(li)
print(li)