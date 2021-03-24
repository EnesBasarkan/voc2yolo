import xml.etree.ElementTree as ET
def readXML(path):
    root = ET.parse(path).getroot()
    print("----------------")
    width, height = int(root[4][0].text), int(root[4][1].text)
    print("width={0} , height{1}".format(width,height))
    xmin, ymin, xmax, ymax = int(root[6][4][0].text), int(root[6][4][1].text), int(root[6][4][2].text), int(root[6][4][3].text)
    print("xmin={0} , ymin={1}, xmax={2}, ymax={3}".format(xmin,ymin,xmax,ymax))
    print(pointNormalizer(xmin,ymin,xmax,ymax,width,height))

def pointNormalizer(xmin,ymin,xmax,ymax,width,height):
    return((xmax-xmin)/2+xmin)/width,((ymax - ymin) / 2 + ymin) / height,(xmax-xmin)/width,(ymax-ymin)/height,

