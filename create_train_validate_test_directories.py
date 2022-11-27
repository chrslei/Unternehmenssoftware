import pandas as pd
import csv
import shutil
import os

'''
# Ordner für Trainingsdaten erstellen
train_directory = "train"
os.mkdir(train_directory)

train_data = pd.read_csv("UTSoftware/train.csv")
folder_names_train = train_data["breed"].unique()

for folder_name in folder_names_train:
    os.mkdir("train/" + folder_name)

filename_train = 'UTSoftware/train.csv'
with open(filename_train, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    next(datareader)

    for row in datareader:
        # Falls Pfad "root" enthält, dann löschen
        if "root" in row[0]:
            row[0] = row[0].replace("root", "")

        file = row[0] + "/" + row[1]
        original = r'UTSoftware/'+file
        target = r'train/'+row[2]+'/'+row[1]
        shutil.copy(original, target)
'''

# Ordner für Validierungsdaten erstellen
validate_directory = "validate"
os.mkdir(validate_directory)

validate_data = pd.read_csv("UTSoftware/validate.csv")
folder_names_validate = validate_data["breed"].unique()

for folder_name in folder_names_validate:
    os.mkdir("validate/" + folder_name)

filename_validate = 'UTSoftware/validate.csv'
with open(filename_validate, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    next(datareader)

    for row in datareader:
        # Falls Pfad "root" enthält, dann löschen
        if "root" in row[0]:
            row[0] = row[0].replace("root", "")

        file = row[0] + "/" + row[1]
        original = r'UTSoftware/'+file
        target = r'train/'+row[2]+'/'+row[1]
        shutil.copy(original, target)

# Ordner für Testdaten erstellen
test_directory = "test"
os.mkdir(test_directory)

test_data = pd.read_csv("UTSoftware/test.csv")
folder_names_test = test_data["breed"].unique()

for folder_name in folder_names_test:
    os.mkdir("test/" + folder_name)

filename_test = 'UTSoftware/test.csv'
with open(filename_test, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    next(datareader)

    for row in datareader:
        # Falls Pfad "root" enthält, dann löschen
        if "root" in row[0]:
            row[0] = row[0].replace("root", "")

        file = row[0] + "/" + row[1]
        original = r'UTSoftware/'+file
        target = r'train/'+row[2]+'/'+row[1]
        shutil.copy(original, target)