__author__ = "Narwhale"
import random
def insert_sort(li):
    for i in range(1,len(li)):
        tem = li[i]
        j = i - 1
        while j >=0 and li[j] > tem:
            li[j+1] = li[j]
            j = j-1
        li[j+1] = tem


data = list(range(1000))
random.shuffle(data)
insert_sort(data)
print(data)