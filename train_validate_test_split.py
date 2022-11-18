import pandas as pd
import csv
import math

# Neue csv-Datei "train.csv", welche die Links zu den Trainingsdaten enthält,
# mit folgende Spaltenüberschriften erstellen: "path", "id", "breed"
with open("UTSoftware/train.csv", 'w', encoding='utf-8', newline="") as csv_train:
    csv_train_writer = csv.writer(csv_train)
    csv_train_writer.writerow(["path", "id", "breed"])

# Neue csv-Datei "validate.csv", welche die Links zu den Validierungsdaten enthält,
# mit folgende Spaltenüberschriften erstellen: "path", "id", "breed"
with open("UTSoftware/validate.csv", 'w', encoding='utf-8', newline="") as csv_validate:
    csv_validate_writer = csv.writer(csv_validate)
    csv_validate_writer.writerow(["path", "id", "breed"])

# Neue csv-Datei "test.csv", welche die Links zu den Testdaten enthält,
# mit folgende Spaltenüberschriften erstellen: "path", "id", "breed"
with open("UTSoftware/test.csv", 'w', encoding='utf-8', newline="") as csv_test:
    csv_test_writer = csv.writer(csv_test)
    csv_test_writer.writerow(["path", "id", "breed"])

# csv-Dateien, dessen Daten zusammengeführt werden sollen, als Dataframe in Programm laden
data = pd.read_csv("UTSoftware/merged.csv")

# Liste erstellen, die jede Hunderasse einmal enthält
list_breeds = data["breed"].unique().tolist()

# Iteriere durch Liste der Hunderassen, um für jede Rasse die Bilder zu train, validate und test aufzuteilen
for breed in list_breeds:

    # Daten einer Hunderasse in eigenes Dataframe speichern
    breed_data = data.loc[data["breed"] == breed]
    # Anzahl der Datensätze auslesen
    breed_counts = breed_data["breed"].value_counts()

    # Wenn mehr als 200 Bilder existieren, dann nur die ersten 200 nehmen und zu 70% zu train, 15% zu validate und 15% zu test
    if breed_counts[0] >= 200:
        # Für Trainings-, Validierungs- und Testset jeweils die Datensätze zuweisen
        train_data = breed_data.iloc[0:140]
        train_data.to_csv("UTSoftware/train.csv", index=False, header=False, mode="a")

        validate_data = breed_data.iloc[140:170]
        validate_data.to_csv("UTSoftware/validate.csv", index=False, header=False, mode="a")

        test_data = breed_data.iloc[170:200]
        test_data.to_csv("UTSoftware/test.csv", index=False, header=False, mode="a")

    # Wenn weniger als 200 Bilder existieren, dann zu 70% zu train, 15% zu validate und 15% zu test aufteilen
    else:
        # absolute Anzahl an Bilder für Trainings-, Validierungs- und Testset bestimmen
        count_train_data = math.floor(breed_counts[0] * 0.7)
        count_validate_data = math.floor(breed_counts[0] * 0.15)
        count_test_data = math.floor(breed_counts[0] * 0.15)

        # Für Trainings-, Validierungs- und Testset jeweils die Datensätze zuweisen
        train_data = breed_data.iloc[0:count_train_data]
        train_data.to_csv("UTSoftware/train.csv", index=False, header=False, mode="a")

        validate_data = breed_data.iloc[count_train_data:count_train_data+count_validate_data]
        validate_data.to_csv("UTSoftware/validate.csv", index=False, header=False, mode="a")

        test_data = breed_data.iloc[count_train_data+count_validate_data:count_train_data+count_validate_data+count_test_data]
        test_data.to_csv("UTSoftware/test.csv", index=False, header=False, mode="a")
