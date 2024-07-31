import numpy as np

# Funktion zur Schätzung
def taxi(N, n, num_simulations=1000):
    estimates = np.zeros((num_simulations, 2))  # Array zur Speicherung der Schätzungen
    
    for i in range(num_simulations):
        y = np.random.choice(N, size=n, replace=True)
        estimate1 = np.max(y)
        estimate2 = 2 * np.mean(y)
        estimates[i] = [estimate1, estimate2]
    
    return estimates

# Simulation
np.random.seed(2021)
num_buses = 500  # Gesamtanzahl der Busse
observed_buses = 10  # Anzahl der beobachteten Busse

# Durchführung der Simulation
estimates = taxi(num_buses, observed_buses)

# Berechnung des Mittelwerts und der Standardabweichung der Schätzungen
mean_estimate1 = np.mean(estimates[:, 0])
sd_estimate1 = np.std(estimates[:, 0])
mean_diff = mean_estimate1 - num_buses
sd_error = sd_estimate1 / np.sqrt(1000)

print(f"Durchschnittliche Schätzung (maximale Nummer): {mean_estimate1:.2f}")
print(f"Standardabweichung der Schätzungen: {sd_estimate1:.2f}")
print(f"Mittlere Abweichung von der Gesamtanzahl: {mean_diff:.2f}")
print(f"Standardfehler der Schätzungen: {sd_error:.2f}")
