__author__ = "Narwhale"

#思路：把列表分成两个部分，一部分有序一部分无序，从无序抽出一位与有序区比较，放在适合的位置

# def insert_sort(alist):
#     """插入排序"""
#     n = len(alist)
#     for j in range(1,n):
#         #range(j,0,-1) --->j,j-1,j-2,j-3...,0
#         for i in range(j,0,-1):
#             if alist[i] < alist[i-1]:
#                 alist[i],alist[i-1] = alist[i-1],alist[i]
#             else:
#                 break

###################################################

def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    #把索引号为0的当做有序区，获取索引号为1的值
    for i in range(1,n):
        #把所获取到的值与前面的有序区的值比较
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                i -= 1
            else:
                break


if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    insert_sort(li)
    print(li)


