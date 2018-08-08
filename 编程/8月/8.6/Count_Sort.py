__author__ = "Narwhale"
#count = [0,0,0,0,0,...,0]
#下标     0,1,2,3,4,...,n

def count_sort(alist,max_num):
    count = [0 for i in range(max_num+1)]
    for num in alist:
        count[num] += 1
    print(count)

    alist.clear()
    for num,m in enumerate(count):
        for j in range(m):
            alist.append(num)
    return alist

import random
data = []
for i in range(100):
    data.append(random.randint(0,100))

print(count_sort(data,100))