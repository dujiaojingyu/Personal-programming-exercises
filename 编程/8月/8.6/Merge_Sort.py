__author__ = "Narwhale"



def merge(alist,first,mid,last):
    low = first
    high = mid + 1
    result = []
    while low <= mid and high <=last:
        if alist[low] < alist[high]:
            result.append(alist[low])
            low += 1
        else:
            result.append(alist[high])
            high += 1

    while low <=mid:
        result.append(alist[low])
        low += 1
    while high <=last:
        result.append(alist[high])
        high += 1
    alist[first:last+1] = result



def merge_sort(alist,first,last):
    if first < last:
        mid = (first + last) // 2
        merge_sort(alist,first,mid)
        merge_sort(alist,mid+1,last)
        merge(alist,first,mid,last)


li = [54,26,93,17,77,31,44,55,20]
merge_sort(li,0,len(li)-1)
print(li)
