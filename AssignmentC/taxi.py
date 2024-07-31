import matplotlib.pyplot as plt
import numpy as np


# Beispiel-Daten
ticket_ids = [2001, 2002, 2004, 2006]
max_ticket_id = max(ticket_ids)
ticket_total_estimate = max_ticket_id + 1

# Visualisierung
plt.figure(figsize=(8, 5))
plt.hist(ticket_ids, bins=np.arange(2000, max_ticket_id+2)-0.5, edgecolor='black')
plt.axvline(x=ticket_total_estimate, color='r', linestyle='--', label=f'Schätzung: {ticket_total_estimate}')
plt.xlabel('Ticket-ID')
plt.ylabel('Häufigkeit')
plt.title('Schätzung der Gesamtanzahl von Teilnehmern')
plt.legend()
plt.show()
