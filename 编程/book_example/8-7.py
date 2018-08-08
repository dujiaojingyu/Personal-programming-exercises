# _*_ coding: utf-8 _*_
#程序 8-7.py (Python 3 version)

import json, datetime

fp = open('earthquake.json','r')
earthquakes = json.load(fp)

print("过去7天全球发生重大的地震信息：")
for eq in earthquakes['features']:
    print("地点:{}".format(eq['properties']['place']))
    print("震级:{}".format(eq['properties']['mag']))
    et = float(eq['properties']['time']) /1000.0
    d=datetime.datetime.fromtimestamp(et).strftime('%Y-%m-%d %H:%M:%S')
    print("时间:{}".format(d))