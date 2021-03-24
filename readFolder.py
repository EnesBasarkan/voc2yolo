from os import listdir
from os.path import isfile, join
import readXML

klasor = "./xml/"

for f in listdir(klasor):
    if(isfile(join(klasor,f))):
        readXML.readXML(klasor+f)
