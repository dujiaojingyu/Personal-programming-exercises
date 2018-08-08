__author__ = "Narwhale"
import os
import os.path
import requests

def download(url):
    '''从指定的 URL 中下载文件并存储到当前目录

    :arg url: 要下载的文件的 URL
    '''
    req = requests.get(url)
    # 首先我们检查是否存在文件
    if req.status_code == 404:
        print('No such file found at %s' % url)
        return
    filename = url.split('/')[-1]
    with open(filename, 'wb') as fobj:
        fobj.write(req.content)
    print("Download over.")

if __name__ == '__main__':
    url = input('Enter a URL: ')
    download(url)