import pandas as pd
import numpy as np

# Funktion zur Berechnung von Cronbachs Alpha
def cronbach_alpha(df):
    items = df.shape[1]
    variances = df.var(ddof=1)
    total_variance = df.sum(axis=1).var(ddof=1)
    alpha = (items / (items - 1)) * (1 - variances.sum() / total_variance)
    return alpha

# CSV-Dateipfad
file_path = 'dataset/job_satisfaction.csv'

# Daten einlesen
df = pd.read_csv(file_path)

# Nur die Frage-Spalten auswählen
df_questions = df[['frage1', 'frage2', 'frage3', 'frage4', 'frage5']]

# Cronbachs Alpha berechnen
alpha = cronbach_alpha(df_questions)
print(f"Cronbachs Alpha: {alpha:.4f}")
