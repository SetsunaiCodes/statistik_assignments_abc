import pandas as pd
import  matplotlib.pyplot as plt
import numpy as np
from csv_reader import read_csv_data


path = "dataset/job_satisfaction.csv"

data = read_csv_data(path)

df = pd.DataFrame(data)

# Korrelationsmatrix berechnen
correlation_matrix = df[['frage1', 'frage2', 'frage3', 'frage4', 'frage5']].corr()

# Korrelationsmatrix ausgeben
print("Korrelationsmatrix:")
print(correlation_matrix)

# Heatmap der Korrelationsmatrix erstellen
plt.figure(figsize=(8, 6))
cax = plt.matshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar(cax)

# Achsenbeschriftungen hinzufügen
plt.xticks(ticks=np.arange(len(correlation_matrix.columns)), labels=correlation_matrix.columns, rotation=45)
plt.yticks(ticks=np.arange(len(correlation_matrix.columns)), labels=correlation_matrix.columns)
plt.title('Korrelationsmatrix', pad=20)

# Werte in der Heatmap anzeigen
for (i, j), val in np.ndenumerate(correlation_matrix.values):
    plt.text(j, i, f'{val:.2f}', ha='center', va='center')

plt.show()