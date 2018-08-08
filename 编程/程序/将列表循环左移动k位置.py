def demo(lst,k):
    x = lst[:k]
    x.reverse()
    print(x)
    y = lst[k:]
    y.reverse()
    print(y)
    r = x + y
    print(r)
    return list(reversed(r))
lst = list(range(1,21))
print(lst)
print(demo(lst,5))

#实际上是将列表循环左移动k位置的算法
def demo(lst,k):
    temp = lst[:]
    for i in range(k)
        temp.append(temp.pop(0))
    return temp

#切片最容易也是最快的

def demo(lst,k):
    return lst[k:] + lst[:k]
