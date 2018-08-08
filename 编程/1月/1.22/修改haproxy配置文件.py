# 1、查
#     输入：www.oldboy.org
#     获取当前backend下的所有记录
#
# 2、新建
#     输入：
#         arg = {
#             'backend': 'www.oldboy.org',
#             'record':{
#                 'server': '100.1.7.9',
#                 'weight': 20,
#                 'maxconn': 30
#             }
#         }
#
# 3、删除
#     输入：
#         arg = {
#             'backend': 'www.oldboy.org',
#             'record':{
#                 'server': '100.1.7.9',
#                 'weight': 20,
#                 'maxconn': 30
#             }
#         }


f1 = open('haproxy','r',encoding= 'utf-8')
f2 = open('haproxy_new','w',encoding= 'utf-8')
file_line = f1.readlines()

select = ("1、请输入搜索的地址：","2、请输入增加的内容：","3、请输入删除的内容：")
for i in select:
    print(i)

num = input('请选择您的操作>>>')

if num == '1':
    data = input('请输入搜索的地址：')
    address = 'backend %s\n'%data
    if address in file_line:
        index = file_line.index(address)

        print(file_line[index].strip())
        print(file_line[index+1])
    else:
        print('您所查询的内容不存在！！')

if num == '2':
    add = input('请输入您要增加的内容：')
    add_content =eval(add)
    add_count = file_line.count('backend %s' %add_content['backend'])
    if add_count == 0:
        for i in file_line:
            f2.write(i)

        f2.write('\nbackend %s' %add_content['backend'])
        f2.write('\n         server %s weight %s maxconn %s' %(add_content['record']['server'],
                                                               add_content['record']['weight'],
                                                               add_content['record']['maxconn']))

    if add_count !=0:
        print('您输入的内容已经存在！！')


if num == '3':
    delete = input('请输入你要删除的内容：')
    delete_eval = eval(delete)

    delete_count = file_line.count('backend %s\n'%delete_eval['backend'])
    if delete_count != 0:
        delete_index = file_line.index("backend www.oldboy.org\n")
        file_line.pop(delete_index)
        file_line.pop(delete_index)

        for line in file_line:
            f2.write(line)
    else:
        print('要删除的内容不存在！')

f1.close()
f2.close()



