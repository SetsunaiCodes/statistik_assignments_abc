import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from csv_reader import read_csv_data

# Dateipfad speichern
file = "dataset/spotify-2023.csv"

data = read_csv_data(file)

# Dataframe aus den Daten erstellen
df = pd.DataFrame(data)

# Konvertiere relevante Spalten in numerische Datentypen
numerical_columns = ['bpm', 'danceability_%', 'valence_%', 'energy_%', 'released_year']
for column in numerical_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# Normalverteilung prüfen
def check_normality(column):
    data = df[column].dropna()  # NaN-Werte entfernen
    k2, p = stats.normaltest(data)
    alpha = 1e-3
    if p < alpha:
        print(f"Die Nullhypothese, dass die Daten in {column} normalverteilt sind, wird abgelehnt (p = {p}).")
    else:
        print(f"Die Nullhypothese, dass die Daten in {column} normalverteilt sind, kann nicht abgelehnt werden (p = {p}).")
    plt.hist(data, bins=10, density=True, alpha=0.6, color='g')
    mu, std = stats.norm.fit(data)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    plt.title(f'Normalverteilung von {column}')
    plt.show()

# T-Test durchführen (z.B. Vergleich von 2023 und anderen Jahren)
def perform_t_test(column, year1, year2):
    group1 = df[df['released_year'] == year1][column].dropna()
    group2 = df[df['released_year'] == year2][column].dropna()
    t_stat, p_value = stats.ttest_ind(group1, group2)
    print(f"T-Test zwischen {year1} und {year2} für {column}: t = {t_stat}, p = {p_value}")

# ANOVA durchführen
def perform_anova(column):
    groups = [group[column].dropna().values for name, group in df.groupby('released_year')]
    f_stat, p_value = stats.f_oneway(*groups)
    print(f"ANOVA für {column}: F = {f_stat}, p = {p_value}")

# Normalverteilung für jede Metrik prüfen
for column in ['bpm', 'danceability_%', 'valence_%', 'energy_%']:
    check_normality(column)

# T-Tests durchführen (z.B. 2023 vs 2019)
for column in ['bpm', 'danceability_%', 'valence_%', 'energy_%']:
    perform_t_test(column, 2023, 2019)

# ANOVA für jede Metrik durchführen
for column in ['bpm', 'danceability_%', 'valence_%', 'energy_%']:
    perform_anova(column)
