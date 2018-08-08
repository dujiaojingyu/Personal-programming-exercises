__author__ = "Narwhale"




__author__ = "Narwhale"
# # alien_color = 'green'
# #
# # if alien_color == 'green':
# #     print('获得5个点')
# #------------------------------
# alien_color = 'red'
# if alien_color == 'green':
#     print('获得5个点')



#-----------------------------------


user_list = ['A','B','C','D','admin']

if user_list:
    for i in user_list:
        if i == 'admin':
            print('Hello admin ,would you like to see a status report?')
        else:
            print('Hello %s,thank you for logging in again'%i)
else:
    print('We need to find some ')