# _*_ coding: utf-8 _*_
# 程序 10-1.py (Python 3 version)

import sqlite3
from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib.pyplot as pt

def disp_menu():
    print("历年油价查询系统")
    print("------------")
    print("1.从网站载入最新油价")
    print("2.显示历年油价信息")
    print("3.最近10周油价信息")
    print("4.油价走势图")
    print("0.结束")
    print("------------")

def fetch_data():
    url = 'http://new.cpc.com.tw/division/mb/oil-more4.aspx'

    html = requests.get(url).text
    sp = BeautifulSoup(html, 'html.parser')
    data = sp.find_all('span', {'id':'Showtd'})
    rows = data[0].find_all('tr')

    prices = list()
    for row in rows:
        cols = row.find_all('td')
        if len(cols[1].text) > 0:
            item = [cols[0].text, cols[1].text, \
                    cols[2].text, cols[3].text]
            prices.append(item)
    for p in prices:
        sqlstr = "select * from prices where gdate='{}';".format(p[0])
        cursor = conn.execute(sqlstr)
        if len(cursor.fetchall()) == 0:
            g92 = 0 if p[1]=='' else float(p[1])
            g95 = 0 if p[2]=='' else float(p[2])
            g98 = 0 if p[3]=='' else float(p[3])
            sqlstr = "insert into prices values('{}', {}, {}, {});". \
                format(p[0], g92, g95, g98)
            print(sqlstr)
            conn.execute(sqlstr)
            conn.commit()


def disp_10data():
    cursor = conn.execute('select * from prices order by gdate desc;')
    n = 0
    for row in cursor:
        print("日期：{}，92无铅：{}，95无铅：{}，98无铅：{}". \
            format(row[0],row[1],row[2],row[3]))
        n = n + 1
        if n == 10:
            break

def chart():
    data = []
    cursor = conn.execute('select * from prices order by gdate;')
    for row in cursor:
        data.append(list(row))
    x = np.arange(0,len(data))
    dataset = [list(), list(), list()]
    for i in range(0, len(data)):
        for j in range(0,3):
            dataset[j].append(data[i][j+1])
    w = np.array(dataset[0])
    y = np.array(dataset[1])
    z = np.array(dataset[2])
    pt.ylabel("NTD$")
    pt.xlabel("Weeks ( {} --- {} )".format(data[0][0], data[len(data)-1][0]))
    pt.plot(x, w, color="blue", label="92")
    pt.plot(x, y, color="red", label="95")
    pt.plot(x, y, color="green", label="98")
    pt.xlim(0,len(data))
    pt.ylim(10,40)
    pt.title("Gasoline Prices Trend")
    pt.legend()
    pt.show()

def disp_alldata():
    cursor = conn.execute('select * from prices order by gdate desc;')
    n = 0
    for row in cursor:
        print("日期：{}，92无铅：{}，95无铅：{}，98无铅：{}". \
            format(row[0],row[1],row[2],row[3]))
        n = n + 1
        if n == 20:
            x = input("请按Enter键继续...(Q:回主菜单)")
            if x == 'Q' or x == 'q': break
            n = 0

conn = sqlite3.connect('gasoline.sqlite')

while True:
    disp_menu()
    choice = int(input("请输入您的选择:"))
    if choice == 0 : break
    if choice == 1: 
        fetch_data()
    elif choice == 2:
        disp_alldata()
    elif choice == 3:
        disp_10data()
    elif choice == 4:
        chart()
    else: break
    x = input("请按Enter键回主菜单")