import csv

# Funktion zum Extrahieren von Zahlenfeldern (gespeichert in einem Dictionary)
def extract_number_fields(filename):
    numerics = {}
    
    with open(filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Erstelle eine Liste aller Felder (Header)
        fieldnames = reader.fieldnames
        
        # Initialisiere das Dictionary mit leeren Listen
        for field in fieldnames:
            numerics[field] = []
        
        for row in reader:
            for key in numerics.keys():
                value = row[key]
                try:
                    # Versuche, das Feld in einen Float zu konvertieren
                    value = float(value)
                    numerics[key].append(value)
                except ValueError:
                    # Falls es nicht konvertiert werden kann, füge None hinzu
                    numerics[key].append(None)

    # Entferne Felder aus dem Dictionary, die keine numerischen Werte enthalten
    numerics = {k: v for k, v in numerics.items() if any(vv is not None for vv in v)}
    return numerics
