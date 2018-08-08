# _*_ coding: utf-8 *_*
# 程序 10-8 (Python 3 version)

from selenium import webdriver

url = 'http://www.jd.com'

web = webdriver.Firefox()
web.get(url)
web.find_element_by_id('ttbar-login').click()
web.find_element_by_name('loginname').clear()
web.find_element_by_name('loginname').send_keys('your account')
web.find_element_by_name('nloginpwd').clear()
web.find_element_by_name('nloginpwd').send_keys('your password')
web.find_element_by_id('loginsubmit').click()
