__author__ = "Narwhale"

def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for j in range(0,n-1):
        for i in range(j+1,0,-1):
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
            else:
                break

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(li)
    print(li)
