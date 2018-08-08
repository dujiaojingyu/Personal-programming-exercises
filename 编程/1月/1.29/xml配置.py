__author__ = "Narwhala"
import xml.etree.ElementTree as ET

tree = ET.parse('xmltest.xml')
root = tree.getroot()
print(root.tag)
# for child in root:
#     print(child.tag,child.attrib)
#     for i in child:
#         print(i.tag,i.text,i.attrib)

for node in root.iter('year'):
    print(node.tag,node.text)