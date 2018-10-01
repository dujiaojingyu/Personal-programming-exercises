__author__ = "Narwhale"

#思路：把列表分成无序区，设置第一个数为有序区，与无序区比较，提取无序区的最小值到有序区

# def select_sort(alist):
#     """选择排序"""
#     n = len(alist)
#     for j in range(0,n-1):
#         min_index = j
#         for i in range(j+1,n):
#             if alist[i] < alist[min_index]:
#                 min_index = i
#         alist[j],alist[min_index] = alist[min_index],alist[j]

##############################################################

def select_sort(alist):
    """选择排序"""
    n = len(alist)
    #提取要比较的数字
    for j in range(0,n-1):
        min_index = j
        #比较无序区的数字得出最小的数字交换位置
        for i in range(1+j,n):
            if alist[i] < alist[min_index]:
                min_index = i
        #数值交换
        alist[j],alist[min_index] = alist[min_index],alist[j]


if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    select_sort(li)
    print(li)

