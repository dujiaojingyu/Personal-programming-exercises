__author__ = "Narwhale"

def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    #递归退出条件
    if n <= 1:
        return alist
    mid = n//2
    #递归分解列表
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])
    #设立左右两个指针为0
    left_pointer = 0
    right_pointer = 0
    result = []
    #循环合并列表
    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] <= right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1
    #当两个列表长度不一样将未走完的列表添加到result中
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]
    return result


li = [54,26,93,17,77,31,44,55,20]
print(li)
m =merge_sort(li)
print(m)
