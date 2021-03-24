def writeFile(point):
    f = open("./txt/{0}.txt".format(point[2].split(".")[0]), "a")
    f.write("{0} {1} {2} {3} {4}\n".format(point[1],round(point[0][0],6),round(point[0][1],6),round(point[0][2],6),round(point[0][3],6)))
    f.close()