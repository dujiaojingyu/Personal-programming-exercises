__author__ = "Narwhale"


def loop_merge_sort(l1, l2):
    temp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            temp.append(l1.pop(0))
        else:
            temp.append(l2.pop(0))

    temp.extend(l1)
    temp.extend(l2)
    return temp

l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10,14,15,78]


l = loop_merge_sort(l1,l2)
print(l)