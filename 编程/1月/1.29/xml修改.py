__author__ = "Narwhala"

import xml.etree.ElementTree as ET

tree = ET.parse('xmltest.xml')
root = tree.getroot()
#修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('updated_by','hsj')

tree.write('xmltest2.xml')


#删除

for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('xmltest3.xml')

