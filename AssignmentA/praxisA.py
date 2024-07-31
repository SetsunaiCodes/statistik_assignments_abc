import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, shapiro, levene
import matplotlib.pyplot as plt

def perform_chi_square_tests(contingency_tables):
    results = []
    for i, table in enumerate(contingency_tables):
        chi2_stat, p_val, dof, ex = chi2_contingency(table)
        results.append({
            'Table': i + 1,
            'Chi2 Stat': chi2_stat,
            'p-value': p_val,
            'Degrees of Freedom': dof
        })
    return results

def test_normality(data):
    results = {}
    for column in data.columns:
        stat, p = shapiro(data[column])
        results[column] = {
            'W-Statistic': stat,
            'p-value': p
        }
    return results

def test_variance_homogeneity(data):
    groups = [data[column] for column in data.columns]
    stat, p = levene(*groups)
    return {
        'Levene Statistic': stat,
        'p-value': p
    }

def main():
    # Beispiel-Kontingenztabellen (5 Tabellen)
    tables = [
        np.array([[10, 20, 30], [6, 9, 12]]),
        np.array([[15, 25], [10, 20]]),
        np.array([[5, 15], [10, 25]]),
        np.array([[20, 30], [15, 25]]),
        np.array([[12, 18], [8, 16]])
    ]

    # Chi-Square Tests
    chi_results = perform_chi_square_tests(tables)
    for result in chi_results:
        print(f"Table {result['Table']}: Chi2 Stat = {result['Chi2 Stat']:.2f}, p-value = {result['p-value']:.4f}")

    # Beispiel-Daten für Normalverteilungstests und Levene-Test
    data = pd.DataFrame({
        'Group1': np.random.normal(0, 1, 100),
        'Group2': np.random.normal(0, 1, 100),
        'Group3': np.random.normal(0, 1, 100)
    })

    # Shapiro-Wilk-Test für Normalverteilung
    normality_results = test_normality(data)
    for column, result in normality_results.items():
        print(f"{column}: W-Statistic = {result['W-Statistic']:.4f}, p-value = {result['p-value']:.4f}")

    # Levene-Test für Homogenität der Varianzen
    levene_result = test_variance_homogeneity(data)
    print(f"Levene Statistic = {levene_result['Levene Statistic']:.4f}, p-value = {levene_result['p-value']:.4f}")

if __name__ == "__main__":
    main()
