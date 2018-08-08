__author__ = "Narwhale"
#选择排序操纵无序区
def select_sort(alist):
    """选择排序"""
    n = len(alist)
    #取有序区
    for j in range(0,n-1):
        min_index = j
        #内层控制无序区的比较
        for i in range(j+1,n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index],alist[j]

if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    select_sort(li)
    print(li)



#1，32，45，23，4，23，5