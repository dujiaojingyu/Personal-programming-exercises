f = open("yesterday","r",encoding="utf-8")
f2 = open("yesterday2","w",encoding="utf-8")

for line in f:
    if  "肆意的快乐等我享受" in line:
        line = line.replace("肆意的快乐等我享受","肆意的快乐等---黄世杰----享受")
    f2.write(line)

f.close()
f2.close()