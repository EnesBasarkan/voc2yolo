import xml.etree.ElementTree as ET


def controlClass(classname):
    file1 = open('classes.txt', 'r+')
    Lines = file1.readlines()
    clsarr = []
    for line in Lines:
        clsarr.append(line.strip())
    print(clsarr)
    if clsarr.count(classname) > 0:
        return clsarr.index(classname)
    else:
        file1.write("\n" + classname)
        controlClass(classname)


def objectLen(path):
    root = ET.parse(path).getroot()
    return len(root)


def readXML(path, i):
    root = ET.parse(path).getroot()
    width, height = int(root[4][0].text), int(root[4][1].text)
    # print("width={0} , height{1}".format(width, height))
    xmin, ymin, xmax, ymax = int(root[i][4][0].text), int(root[i][4][1].text), int(root[i][4][2].text), int(
        root[i][4][3].text)
    # print("xmin={0} , ymin={1}, xmax={2}, ymax={3}".format(xmin, ymin, xmax, ymax))
    return pointNormalizer(xmin, ymin, xmax, ymax, width, height), str(controlClass(root[6][0].text)), root[1].text


def pointNormalizer(xmin, ymin, xmax, ymax, width, height):
    return ((xmax - xmin) / 2 + xmin) / width, ((ymax - ymin) / 2 + ymin) / height, (xmax - xmin) / width, (
            ymax - ymin) / height
