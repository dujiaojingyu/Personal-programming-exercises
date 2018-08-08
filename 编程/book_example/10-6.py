# _*_ coding: utf-8 *_*
# 程序 10-6 (Python 3 version)

from selenium import webdriver
urls = [
'http://www.sina.com.cn',
'http://www.sohu.com',
'http://www.eastmoney.com',
'http://www.newone.com.cn',
'https://www.baidu.com']

web = webdriver.Firefox()
web.set_window_position(0,0)
web.set_window_size(800,600)
i = 0
for url in urls:
    web.get(url)
    web.save_screenshot("webpage{}.png".format(i))
    i += 1
web.quit()
