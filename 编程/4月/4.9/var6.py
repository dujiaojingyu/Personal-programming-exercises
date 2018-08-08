__author__ = "Narwhale"

# hsj_information = {
#     'first_name':'H',
#     'last_name':'sj',
#     'age':'22',
#     'city':'shanghai',
# }
#
# hhj_information = {
#     'first_name':'H',
#     'last_name':'hj',
#     'age':'34',
#     'city':'shenzhen',
# }
#
# hfg_information = {
#     'first_name':'H',
#     'last_name':'fg',
#     'age':'24',
#     'city':'guangzhou',
# }
#
# people = [hsj_information,hhj_information,hfg_information]
#
# for i in people:
#     info = '''
#         first_name: %s
#         last_name: %s
#         age: %s
#         city: %s
#     ''' % (i['first_name'],
#            i['last_name'],
#            i['age'],
#            i['city'])
#     print(info)
#


#--------------------------------------

#
# wangcai = {
#     'type':'dog',
#     'host':'hsj'
# }
#
# xiaohua = {
#     'type':'cat',
#     'host':'xl'
# }
#
# huahua = {
#     'type':'fish',
#     'host':'lh'
# }
#
# pets = [wangcai,xiaohua,huahua]
#
# for i in pets:
#     info = '''
#         type: %s
#         host: %s
#     '''%(i['type'],i['host'])
#     print(info)




#--------------------------------------


favorite_places = {
    'hsj':['shanghai','beijing','guangzhou'],
    'wjh':['xinjiang','wulumuqi','tianjing'],
    'xyy':['foshan','zhuhai','shenzhen']
}

for people,places in favorite_places.items():
    print('\n'+'people:',people)
    print('favorite places:')
    for i in places:
        print(i)
