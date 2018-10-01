__author__ = "Narwhale"


def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for j in range(gap,n):
            while j > 0:
                if alist[j] < alist[j-gap]:
                    alist[j],alist[j-gap] = alist[j-gap],alist[j]
                    j -= gap
                else:
                    break
        gap = gap // 2


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(li)
print(li)


