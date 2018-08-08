__author__ = "Narwhale"

def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1,n):
        for i in range(j,0,-1):
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
            else:
                break

if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    insert_sort(li)
    print(li)

#j=1,i=0
#j=2,i=1
#j=3,i=2
#j=4,i=3