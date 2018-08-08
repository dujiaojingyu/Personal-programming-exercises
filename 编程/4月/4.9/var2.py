__author__ = "Narwhale"

# current_users = ['A','B','C','D','admin','F','G','H','J']
# new_users = ['A','R','Q','B','L']
#
# for i in new_users:
#     if i in current_users:
#         print('用户名已存在，请重新输入')
#     else:
#         print('此用户名可以使用')


#-----------------------------------

current_users = ['Ai','B','C','D','admin','F','G','H','J']
new_users = ['AI','R','Q','B','L']
current_users = [username.upper() for username in current_users]

for i in new_users:
    if i.upper() in current_users:
        print('用户名已存在，请重新输入')
    else:
        print('此用户名可以使用')