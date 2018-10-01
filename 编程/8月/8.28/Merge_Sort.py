__author__ = "Narwhale"

def merge_sort(alist):
    """归并排序"""
    #先分解在合并
    n = len(alist)
    if n == 1:
        return alist
    mid = n // 2
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])

    left_pointer = 0
    right_pointer = 0
    result = []

    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] <= right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1
    result.extend(left_list[left_pointer:])
    result.extend(right_list[right_pointer:])
    return result


if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    m =merge_sort(li)
    print(m)
