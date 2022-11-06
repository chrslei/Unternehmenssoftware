import os
import numpy as np
import pandas as pd
from xml.etree import ElementTree
import csv
import glob


# hier eine CSV File erstellen
# dann hier die csv file öffnen und auf write setzen

csvfile = open("UTSoftware/data1.csv", 'w', encoding='utf-8')
#hier wird der writer für die csv file erstellt
csvfile_writer = csv.writer(csvfile)
#hier bekommt die csv file seinen Header
csvfile_writer.writerow(["root", "id", "breed"])

#die root wo die Annotationen stehen werden hier in die Liste fold geschrieben
fold = []
for folders in os.listdir("UTSoftware/Dataset_1/Low-Annotations"):
    fold.append(folders)

#print(fold)
#erste Schleife nimmt dann von low Annotations einen Ordner
#liest dann mit glob glob die ganzen Filenames im Ordner die mit xml enden aus und erstellt eine Liste davon
for f in fold:
    r = "UTSoftware/Dataset_1/Low-Annotations/" + f + "/*.xml"
    roots = glob.glob(r)
    # print(r)
    # hier wird dann jedes xml geparst und folder, filename und die Rasse ausgelesen und in die CSV geschrieben
    for root in roots:
        xml = ElementTree.parse(root)
        folder = xml.findtext("folder")
        filename = xml.findtext("filename")
        nameU = folder.split("-")
        name = nameU[2]
        csv_line = [folder, filename, name]
        csvfile_writer.writerow(csv_line)
