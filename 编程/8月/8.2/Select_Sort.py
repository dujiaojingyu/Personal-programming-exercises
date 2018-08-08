__author__ = "Narwhale"

def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(0,n-1):
        min_index = j
        for i in range(j+1,n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[min_index],alist[j]= alist[j],alist[min_index]

if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    select_sort(li)
    print(li)
