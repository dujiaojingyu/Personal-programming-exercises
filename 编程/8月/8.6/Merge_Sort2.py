__author__ = "Narwhale"


def merge_sort(alist):
    """归并排序"""
    #先分解
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    #需要接受列表
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])

    #再合并
    result = []
    left_pointer,right_pointer =0,0
    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] < right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]
    return result


li = [54,26,93,17,77,31,44,55,20]
print(li)
m =merge_sort(li)
print(m)



