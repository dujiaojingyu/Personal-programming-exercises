__author__ = "Narwhale"


def binary_search(alist,item):
    """二分查找"""
    low = 0
    high = len(alist) - 1
    while low <= high:
        mid = (low + high) // 2
        if alist[mid] == item:
            return mid
        elif alist[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return
a = [1,2,3,5,6,7]

b = binary_search(a,0)
print(b)