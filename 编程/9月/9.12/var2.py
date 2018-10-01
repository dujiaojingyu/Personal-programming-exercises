__author__ = "Narwhale"
import linecache

#数据处理
fields=('bid','uid','username','v_class','content','img','time','source','rt_num','cm_num','rt_uid'
    ,'rt_username','rt_v_class','rt_content','rt_img','src_rt_num','src_cm_num','gender','rt_mid'
    ,'location','rt_mid','mid','lat','lon','lbs_type','lbs_title','poiid','links','hashtags','ats'
    ,'rt_links','rt_hashtags','rt_ats','v_url','rt_v_url')

keys = {fields[k]:k for k in range(0,len(fields))}

f = linecache.getlines('twitter数据挖掘片段.txt')       #返回的是以每行字符串为元素的列表形式，可以通过索引取得数据
# print(f[0])
lines = [x[1:-1].split(',') for x in f]
