__author__ = "Narwhale"
#
# def select_sort(alist):
#     """选择排序"""
#
#     n = len(alist)
#     for j in range(0,n-1):
#         min_index = j
#         for i in range(j+1,n):
#             if alist[min_index] > alist[i]:
#                 min_index = i
#
#         alist[min_index],alist[j] = alist[j],alist[min_index]
#
# li = [54,26,93,17,77,31,44,55,20]
# select_sort(li)
# print(li)


###################################


def select_sort(alist):
    n = len(alist)
    #外层循环，控制要交换多少次
    for j in range(0,n-1):
        #内层循环
        #初定索引号为0的数字最小，让它和其他数值比较出最小的交换位置
        min_index = j
        for i in range(j+1,n):
            if alist[min_index] > alist[i]:
                #交换最小索引的标识
                min_index = i
        #退出内循环之后才进行位置交换
        alist[j],alist[min_index] = alist[min_index],alist[j]

#j=0      min_index=0      (1,n)--->(0+1,n)--->(j+1)
#j=1      min_index=1      (2,n)--->(1+1,n)--->(j+1)
#j=2      min_index=2      (3,n)--->(2+1,n)--->(j+1)
#j=3      min_index=3      (4,n)--->(3+1,n)--->(j+1)

if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    select_sort(li)
    print(li)
