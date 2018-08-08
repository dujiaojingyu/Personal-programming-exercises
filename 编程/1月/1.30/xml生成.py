__author__ = "Narwhale"

from xml.etree import ElementTree as ET
def build_sitemap():
    urlset = ET.Element("urlset")       # ET.Element创建一个根节点，标签为urlset
    url = ET.SubElement(urlset,"url")   # ET.SubElement在根节点urlset下建立子节点
    loc = ET.SubElement(url,"loc",attrib={"name":"百度"})         #attrib为创建属性
    loc.text = "http://www/baidu.com"                             #loc.test 为写入内容
    time = ET.SubElement(url,"time")
    time.text = "2018-1-30"
    change = ET.SubElement(url,"change")
    change.text = "daily"
    priority = ET.SubElement(url,"priority")
    priority.text = "1.0"
    tree = ET.ElementTree(urlset)
    tree.write("set.xml",'utf-8')         #写入时加上‘utf-8’可以转译中文，不会有乱码
if __name__ == '__main__':
    build_sitemap()