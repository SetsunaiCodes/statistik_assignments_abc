from csv_reader import read_csv_data
from extract_numerics import extract_number_fields
import statistics

# Durchschnitt ausrechnen
def calculate_mean(column_data):
    return statistics.mean(column_data)

# Median ausrechnen
def calculate_median(column_data):
    return statistics.median(column_data)

# Modus ausrechnen
def calculate_mode(column_data):
    return statistics.mode(column_data)

# Varianz ausrechen
def calculate_variance(column_data):
    return statistics.variance(column_data)    
  
# Main Methode (CSV auslesen und entsprechende Funktion aufrufen)
def main():
    file = 'datasets/ashesOfWar.csv'
    numerics_columns = extract_number_fields(file)

    for columns, values in numerics_columns.items():
        if values:
            print(f"Statistik für: {columns}:")
            print(f"Durchschnitt: {calculate_mean(values)}")
            print(f"Median: {calculate_median(values)}")
            print(f"Modus: {calculate_mode(values)}")
            print(f"Varianz: {calculate_variance(values)}")
            print("------------------------------")

# Init Python
if __name__ == "__main__":
    main()