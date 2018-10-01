__author__ = "Narwhale"

import re
import requests
url = "https://book.douban.com/"

content = requests.get(url).text
print(content)
res_obj = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?publisher">(.*?)</span>.*?</li>',re.S)
print(res_obj)
results = res_obj.findall(content)
print(results)
f = open('douban.txt','w',encoding='utf-8')
for result in results:
    url,name,author,date,publisher = result
    f.write(url)
    f.write(name)
    f.write(author)
    f.write(date)
    f.write(publisher)

f.close()