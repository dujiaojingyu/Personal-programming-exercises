for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d=%d" % (i, j, i * j))


#第二种解法
for i in range(1,10):
    for j in range(1,10):
        print(j, "x", i, "=", i * j,"\t",end="")
        if i==j:
            print("")
            break