__author__ = "Narwhale"

import urllib
#urllib.request  请求
#urllib.error    错误信息
#urllib.response 响应
#urllib.parse    解析

data = bytes(urllib.parse.urencode({'hello':'world'}))

