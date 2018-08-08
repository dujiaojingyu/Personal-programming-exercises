__author__ = "Narwhale"

def merge_sort(alist):
    """归并排序"""
    #先分解
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    #以mid为界限分成左右两边新的子序列
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])
    #紧接着将两个有序子序列合并
    # merge(left_list,right_list)
    left_pointer,right_pointer = 0, 0
    result = []

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
