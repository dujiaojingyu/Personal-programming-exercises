__author__ = "Narwhale"


#思路：将第一个数当成为有序序列，然后将这个数与其他数比较，当其他数小于它交换索引号，循环一遍得歘最小数
#将第一个数的位置与最小数的位置调换。

def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(0,n-1):
        min_value = j
        for i in range(j+1,n):
            if alist[i] < alist[min_value]:
                min_value = i
        alist[j],alist[min_value] = alist[min_value],alist[j]


if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    select_sort(li)
    print(li)

