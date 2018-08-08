import random
def demo(lst):
    m = min(lst)
    result = (m,)
    d = [lst.index(m)]
    result = result + tuple(d)
    return result
lst = [random.randint(1,20) for i in range(50)]
print(lst)
print(demo(lst))