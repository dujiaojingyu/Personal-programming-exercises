__author__ = "Narwhale"

def binary_search(alist,item):
    """二分查找"""
    n = len(alist)
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high) // 2
        if alist[mid] == item:
            return mid
        elif alist[mid] > item:
            high = mid -1
        else:
            low =mid + 1
    return


a = [1,2,3,4,5,6,7,8,9,45,47,56,87,89]

b = binary_search(a,8)
print(b)
