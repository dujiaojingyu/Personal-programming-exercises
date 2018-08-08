__author__ = "Narwhale"
string = input("请输入字符串：")
length = len(string)
count = 1
if string != string.upper():
    count = 0
for i in range(length-1):
    if string[i] == string[i+1]:
        count = 0
for i in range(length-3):
    x1 = string.find(string[i],i+2)
    if x1 == -1:
        continue
    else:
        for j in range((i+1),x1):
            x2 = string.find(string[j],(x1+1))
            if x2 > 0:
                count = 0
                break
if count ==0:
    print("Dislikes")
elif count==1:
    print("Likes")