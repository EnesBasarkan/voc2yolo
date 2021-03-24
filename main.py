import xml.etree.ElementTree as ET
root = ET.parse('xml/1.xml').getroot()
print("----------------")
width, height = int(root[4][0].text), int(root[4][1].text)
print("width={0} , height{1}".format(width,height))
xmin, ymin, xmax, ymax = int(root[6][4][0].text), int(root[6][4][1].text), int(root[6][4][2].text), int(root[6][4][3].text)
print("xmin={0} , ymin={1}, xmax={2}, ymax={3}".format(xmin,ymin,xmax,ymax))
