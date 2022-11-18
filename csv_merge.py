import csv
import pandas as pd

# csv-Dateien, dessen Daten zusammengeführt werden sollen, als Dataframes in Programm laden
data1 = pd.read_csv("UTSoftware/data1.csv")
data2 = pd.read_csv("UTSoftware/data2.csv")

# in beiden Dataframes werden jeweils in Spalte "root" der relative Pfad zum jeweiligen Ordner,
# wo sich das Bild befindet, hinterlegt
data1["root"] = "Dataset_1/low-resolution/" + data1["root"]
data2["root"] = "Dataset_2/images/" + data2["root"]

# Neue csv-Datei "merged.csv" mit folgende Spaltenüberschriften erstellen: "path", "id", "breed"
with open("UTSoftware/merged.csv", 'w', encoding='utf-8', newline="") as csv_merge:
    csv_merge_writer = csv.writer(csv_merge)
    csv_merge_writer.writerow(["path", "id", "breed"])

# Datensätze aus data1 (=data1.csv) und data2 (=data2.csv) zu merged.csv hinzufügen. Datensätze sind nun vereinigt
data1.to_csv("UTSoftware/merged.csv", index=False, header=False, mode="a")
data2.to_csv("UTSoftware/merged.csv", index=False, header=False, mode="a")

print(data1.value_counts())


