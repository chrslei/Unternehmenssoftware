# Unternehmenssoftware

## 1. Datensätze
Downloade beide Datensätze und speichere sie in einem Unterordner "UTSoftware" in dem Ordner wo du das Projekt hast. 

Datenset 1 downloade bitte low-resolution und low-annotaions in einem Unterordner Dataset_1:
Dataset_1: https://cg.cs.tsinghua.edu.cn/ThuDogs/

Datenset 2: downloade files: images.tar.gz (dataset) and annotations.tar.gz (groundtruth data) in einem Unterordner Dataset_2 
Dataset_2: https://www.robots.ox.ac.uk/~vgg/data/pets/

## 2. CSV Datei erstellen und die Annotaionen auslesen und Pfade erstellen 
 Für Datensatz 1: 
 Erstelle eine leere CSV-Datei (data1.csv) in dem Ordner UTSoftware. 
 Beachte hier dazu, dass du den Code in der Python File annotaions_in_csv_file_dataset1 im folgenden anpassen musst, wenn du andere Dateinamen verwendest: 
        ....    csvfile = open("Ordnername/CSV_Dateiname.csv", 'w', encoding='utf-8')
 Führe das Python File aus. 
 
 Für Datensatz 2: 
 Erstelle eine leere CSV-Datei (data2.csv) in dem Ordner UTSoftware. 
 Beachte hier dazu, dass du den Code in der Python File annotaions_in_csv_file_dataset1 im folgenden anpassen musst, wenn du andere Dateinamen verwendest: 
         ....    csvfile = open("Ordnername/CSV_Dateiname.csv", 'w', encoding='utf-8')
 Führe das Python File aus. 

## 3.Merge beide CSV aus Schritt 2. 
Dazu führst du den Code aus csv_merge.py aus. 


## 4. erstelle train, test, validate CSV Dateien: 
Hier führst du den Code aus train_validate_test_split.py 
 
## 5. Verschiebe die Bilder in die jeweiligen train, test oder validate Ordner 
Hier einfach die create_train_validate_test_directories.py ausführen. 

## 6. merge Hunderassen_ordner die ähnlich geschrieben wurden in einen Ordner 
Führe mergeDirectory.py aus. 

## 7. zippe die Ordner train, test, validate und lade sie in dein Google Drive hoch 

## für das nicht vortrainierte Modell: https://github.com/MilenaKalo/breedClassification.git 
hier dann ein colab Notebook erstellen und den Code einfügen und ausführen.

## für das vortrainierte Modell: https://github.com/MilenaKalo/preTrainedModel.git
hier dann ein colab Notebook erstellen und den Code einfügen und ausführen.

