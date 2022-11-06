import os
import numpy as np
import pandas as pd
from xml.etree import ElementTree
import csv
import glob

#function that splits string at first number
def split_string_at_first_number(string):
    return [s for s in string.split() if s.isdigit()]


# hier eine CSV File erstellen
# dann hier die csv file öffnen und auf write setzen

csvfile = open("UTSoftware/data2.csv", 'w', encoding='utf-8')
#hier wird der writer für die csv file erstellt
csvfile_writer = csv.writer(csvfile)
#hier bekommt die csv file seinen Header
csvfile_writer.writerow(["root", "id", "breed"])

#die root wo die Annotationen stehen werden hier in die Liste fold geschrieben
fold = []
for folders in os.listdir("UTSoftware/Dataset_2/annotations"):
    fold.append(folders)

#print(fold)
#erste Schleife nimmt dann von low Annotations einen Ordner
#liest dann mit glob glob die ganzen Filenames im Ordner die mit xml enden aus und erstellt eine Liste davon
for f in fold:
    r = "UTSoftware/Dataset_2/annotations/" + f + "/*.xml"
    roots = glob.glob(r)
    # print(r)
    # hier wird dann jedes xml geparst und folder, filename und die Rasse ausgelesen und in die CSV geschrieben
    for root in roots:
        xml = ElementTree.parse(root)
        #print(xml.findtext("filename"))
        #print(xml.getroot().find("object").find("name").text)

        #gibt nur alle daten mit mit tag "dog" aus
        if xml.getroot().find("object").find("name").text == "dog":
            filename = xml.findtext("filename")
            nameU = xml.findtext("filename").split('_')
            nameU.remove(nameU[-1])
            name = ""
            print(nameU)
            for s in nameU:
                name = name + s + "_"
            name = name[:-1].lower()
            folder = "root"
            csv_line = [folder, filename, name]
            csvfile_writer.writerow(csv_line)