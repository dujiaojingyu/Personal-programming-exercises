__author__ = "Narwhale"

def quick_sort(alist,first,last):
    """快速排序"""
    #递归的退出条件
    if first >= last:
        return
    low = first
    high = last
    #获取第一个数为要排序的数
    mid_value = alist[first]
    while low < high:
        #先走左右边，当右边数大于mid_value时左边数减一
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        # 再走左边，当左边数小于mid_value时左边数加一
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    #最后当low和high相等时结束循环将mid_value数放在low和high相等的地方
    alist[low] = mid_value
    #递归执行
    quick_sort(alist,first,low-1)
    quick_sort(alist,low+1,last)


li = [54,26,93,17,77,31,44,54,55,20]
quick_sort(li,0,len(li)-1)
print(li)