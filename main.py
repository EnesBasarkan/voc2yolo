from os import listdir
from os.path import isfile, join
import readXML
import writeFile

klasor = "./xml/"

for f in listdir(klasor):
    if(isfile(join(klasor,f))):
        print(readXML.objectLen(klasor+f))
        for i in range(6,readXML.objectLen(klasor+f)):
            writeFile.writeFile(readXML.readXML(klasor+f,i))