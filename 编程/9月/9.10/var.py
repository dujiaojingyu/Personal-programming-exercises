__author__ = "Narwhale"



# def bubble_sort(alist):
#     """冒泡排序"""
#     n = len(alist)
#     for j in range(0,n-1):
#     #内层
#         for i in range(0,n-1-j):
#             if alist[i] > alist[i+1]:
#                 alist[i],alist[i+1] = alist[i+1],alist[i]
#
#
# li = [54,26,93,17,77,31,44,55,20]
# bubble_sort(li)
# print(li)



# def insert_sort(alist):
#     """插入排序"""
#     n = len(alist)
#
#     for i in range(1,n):
#         while i > 0:
#             if alist[i] < alist[i-1]:
#                 alist[i],alist[i-1] = alist[i-1],alist[i]
#                 i -= 1
#             else:
#                 break
#
# if __name__ == "__main__":
#     li = [54,26,93,17,77,31,44,55,20]
#     insert_sort(li)
#     print(li)


# def merge_sort(alist):
#     """归并排序"""
#     #先分解在合并
#     n = len(alist)
#     if n == 1:
#         return alist
#     mid = n // 2
#     left_list = merge_sort(alist[:mid])
#     right_list = merge_sort(alist[mid:])
#
#
#     result = []
#     left_prointer = 0
#     right_prointer = 0
#
#     while left_prointer < len(left_list) and right_prointer < len(right_list):
#         if left_list[left_prointer] <= right_list[right_prointer]:
#             result.append(left_list[left_prointer])
#             left_prointer += 1
#         else:
#             result.append(right_list[right_prointer])
#             right_prointer += 1
#     result.extend(left_list[left_prointer:])
#     result.extend(right_list[right_prointer:])
#
#     return result
#
#
# if __name__ == "__main__":
#     li = [54,26,93,17,77,31,44,55,20]
#     print(li)
#     m =merge_sort(li)
#     print(m)
#
#
def quick_sort(alist,first,last):
    """快速排序"""
    pass

if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,54,55,20]
    quick_sort(li,0,len(li)-1)
    print(li)


#
# def select_sort(alist):
#     """选择排序"""
#     pass
#
#
# if __name__ == "__main__":
#     li = [54,26,93,17,77,31,44,55,20]
#     select_sort(li)
#     print(li)
#
#
#
#
# def shell_sort(alist):
#     """希尔排序"""
#     pass
#
# li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# shell_sort(li)
# print(li)
