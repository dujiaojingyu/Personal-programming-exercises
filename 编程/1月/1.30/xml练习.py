__author__ = "Narwhala"

import xml.etree.ElementTree as ET
tree = ET.parse('xmltest.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)


for neighbor in root.iter('neighbor'):
    print(neighbor.attrib['name'])