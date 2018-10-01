__author__ = "Narwhale"

#插入排序思路：将列表分成两各部分，一部分看成有序，一部分看成无序，从无序中抽取数据与有序区的数字比较
#当比较到适合的位置将其插入到该位置。

def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    #控制无序区
    for j in range(1,n):
        #控制有序区
        for i in range(j,0,-1):
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(li)
    print(li)
