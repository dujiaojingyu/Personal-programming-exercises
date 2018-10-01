__author__ = "Narwhale"

import re
import requests
from config import *
from pyquery import PyQuery as pq
from urllib.parse import urlencode


base_url = 'http://weixin.sogou.com/weixin?'

headers = {
    'Cookie': 'IPLOC=CN4418; SUID=B3A54A713020910A000000005BAC2F91;\
         SUV=1538011025994207; ABTEST=0|1538011029|v1; \
         weixinIndexVisited=1; JSESSIONID=aaaEZSJ1I9a-X8v5WbCvw; ppinf=5\
         |1538011064|1539220664|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmF\
         tZTo4Ok5hcndoYWxlfGNydDoxMDoxNTM4MDExMDY0fHJlZm5pY2s6ODpOYXJ3aGFsZX\
         x1c2VyaWQ6NDQ6bzl0Mmx1SmdqRDltbmd6VTZsWnlmNE1rdk95a0B3ZWl4aW4uc29odS\
         5jb218; pprdig=WSLfaKIhy5arBjdR5uu6iK15lrv5Y62-zV9OPL3-DZnWddTI_sgj4x\
         BvuYCc3nJ3-k8jVB6utOB9g3N5ZUDZC2SrLt8A36sGfbGHQTn8Vkjpv7m8EGhoMpx4ieMd\
         3_TQxRXKy68ge8MejI9atXNcshtgYNZcrgQmfI2K4eaFX6E; sgid=23-37259383-AVusL\
         7g2YS9Nibgju52xv9OI; ppmdig=15380110640000008247aa1f35d6ff310f9548a28264\
         240c; PHPSESSID=unve3m93ekv1hkno7ldr76a8o0; SUIR=988E615B2A2E5DFB333FC58A2\
         B36E7C9; SNUID=5F49A19DECE99D3CCD735E31EC8FDDBE; sct=3',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
}

def get_html(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except Exception:
        return get_html(url)

def get_index():
    data = {
        'type': '2',
        's_from': 'input',
        'query': '风景',
        'ie': 'utf8',
        '_sug_': 'n',
        '_sug_type_':'',
    }
    #转换成get请求数据
    querys = urlencode(data)
    url = base_url + querys
    # print(url)
    html = get_html(url)
    return html


def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list h3 a').items()
    for item in items:
        yield item.attr('href')

# def get_detail_html(url):


def main():
    html = get_index()
    article_urls = parse_index(html)
    for article_url in article_urls:
        print('href:',article_url)


if __name__ == '__main__':
    main()