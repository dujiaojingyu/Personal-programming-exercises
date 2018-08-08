__author__ = "Narwhale"

while True:
    username = input('请输入名字：')
    with open('username.txt', 'a') as f:
        if len(username):
            f.write(username+'\n')