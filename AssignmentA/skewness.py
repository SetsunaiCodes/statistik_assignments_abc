import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew
from extract_numerics import extract_number_fields

def main():
    path = "datasets/sorceries.csv"
    numerics = extract_number_fields(path)
    
    # Konvertiere das Dictionary in einen DataFrame und fülle fehlende Werte auf
    df = pd.DataFrame.from_dict(numerics).fillna(method='ffill').fillna(method='bfill')
    
    if 'INT' not in df.columns:
        print("Fehler: 'INT'-Spalte existiert nicht im Datensatz.")
        return
    
    # Konvertieren der 'INT'-Spalte in numerische Werte (um sicher zu gehen)
    df['INT'] = pd.to_numeric(df['INT'], errors='coerce')
    
    # Entfernen von NaN-Werten, die durch nicht-konvertierbare Werte entstehen können
    df = df.dropna(subset=['INT'])
    
    int_values = df['INT']
    
    # Berechnung der Schiefe
    skewness = skew(int_values)

    # Visualisierung
    plt.figure(figsize=(10, 6))
    plt.hist(int_values, bins=10, edgecolor='black', alpha=0.7)
    plt.title('Histogramm der INT-Werte')
    plt.xlabel('INT')
    plt.ylabel('Häufigkeit')
    plt.axvline(int_values.mean(), color='red', linestyle='dashed', linewidth=1)
    plt.text(int_values.mean() + 0.5, max(plt.gca().get_ylim()) * 0.9, 'Mean', color='red')

    # Schiefe anzeigen
    plt.figtext(0.15, 0.85, f'Schiefe: {skewness:.2f}', fontsize=12)

    plt.show()

# Init Python
if __name__ == "__main__":
    main()
