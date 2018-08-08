# _*_ coding: utf-8 _*_
# 程序 12-3 (Python 2 Version)

import facebook

token = 'CAACEdEose0cBAFTD3DB8NrkDrVmQTH9esEZBTECpxInfKQTric2BNDDv3YgwdhfxfCZAXNfQy5gY0k8obkptR1K9RnQG1PwGMu4zqsltxHLcm5zPZBLbQInmEUHjtOhV4qxt5fFmAd0vtWMJjh0JZCoS5vj7ZBDIUe7AjnqRhosqZBfhszZAHZBgyJc3FxZCvDhZAsb3PokhzAiSuBZBl1KdmcH'

g = facebook.GraphAPI(access_token=token)

attachment =  {
	'name': '股票行情网址分享', 
	'link': 'http://www.eastmoney.com/',
	'caption': '查行情',
	'description': '东方财富网是中国访问量最大、影响力最大的财经证券门户网站之一。这里做一个简单的接口让大家方便使用。',
	'picture': ' http://g1.dfcfw.com/g1/img2011/logo_comm.gif '
}

g.put_wall_post(message='这是使用 Python facebook-sdk 测试发表消息的范例', attachment=attachment)


