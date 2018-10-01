__author__ = "Narwhale"

import time

#数据准备
# fields=['bid','uid','username','v_class','content','img','time','source','rt_num','cm_num','rt_uid'
#     ,'rt_username','rt_v_class','rt_content','rt_img','src_rt_num','src_cm_num','gender','rt_mid'
#     ,'location','rt_mid','mid','lat','lon','lbs_type','lbs_title','poiid','links','hashtags','ats'
#     ,'rt_links','rt_hashtags','rt_ats','v_url','rt_v_url']
# with open('text.txt','w',encoding='utf-8') as f_write:
#     with open('twitter数据挖掘片段.txt','r',encoding='utf-8') as f_read:
#         for line in f_read:
#             line = eval(line)
#             dict_line_twitter = dict(zip(fields,line))
#             f_write.write(str(dict_line_twitter)+'\n')

# g = [1,2,3,4,5,6,7]
# w = open('xxx.txt','w',encoding='utf-8')
# d = open('sss.txt','r',encoding='utf-8')
# for i in d:
#     print(type(eval(i)))
#     i = eval(i)
#     # l = i.strip().split(',')
#     dict_l = dict(zip(g,i))
#     w.write(str(dict_l)+'\n')
##############################################################
# 1.该文本里，有多少个用户。（要求：输出为一个整数。）

# set_username = set() #空集合
# with open('text.txt','r',encoding='utf-8') as f_read:
#     for line in f_read:
#         line = eval(line)
#         set_username.update([line['username']])
#     print(list(set_username))
#     print(len(set_username))
# #


########################################################
#2.该文本里，每一个用户的名字。 （要求：输出为一个list。）
# set_username = set() #空集合
# with open('text.txt','r',encoding='utf-8') as f_read:
#     for line in f_read:
#         line = eval(line)
#         set_username.update([line['username']])
#     print(list(set_username))
#     print(len(set_username))


#######################################################################
#3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）
# count = 0
# with open('text.txt','r',encoding='utf-8') as f_read:
#     for line in f_read:
#         line = eval(line)
#         if line['time'].startswith('2012-11'):
#             count += 1
# print(count)

######################################################################

#4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）
with open('text.txt','r',encoding='utf-8') as f_read:
    pass