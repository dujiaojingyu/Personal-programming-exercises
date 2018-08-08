__author__ = "Narwhale"
import random
def bobben_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]



data = list(range(1000))
random.shuffle(data)
bobben_sort(data)
print(data)