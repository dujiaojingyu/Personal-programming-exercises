import random

def hongbao(toltal,num):
    each = []
    already = 0
    for i in range(1,num):
        t = random.randint(1,(toltal-already)-(num-i))
        each.append(t)
        already = already + t
    each.append(toltal-already)
    return each

if __name__ == "__main__":
    toltal = 30
    num = 5
    for i in range(30):
        each = hongbao(toltal,num)
        print(each)