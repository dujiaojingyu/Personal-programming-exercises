__author__ = "Narwhale"


''''文件处理模块'''
import json,os,time,sys
conf_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(conf_path)
from conf import settings

# print(settings.DATABASE)
def file_path():
    '''
    返回文件路径
    :return:
    '''
    settings_params = settings.DATABASE
    db_path = '%s\%s' % (settings_params['path'], settings_params['name'])
    return db_path

def file_db_handle(name):
    db_path = file_path()
    print(db_path)
    with open('%s\%s.json'%(db_path,name),'r') as f:    #可以检测文件名然后分割文件名在传进去
        data = json.load(f)
    # print(type(data))
    return data

# file_db_handle()



