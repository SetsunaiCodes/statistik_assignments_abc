import csv

# Data Reader CSV (geispeichert in Array)
def read_csv_data(path):
    data=[]
    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data