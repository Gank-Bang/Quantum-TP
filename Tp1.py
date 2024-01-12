import os
from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Création d'un circuit avec 3 qbits : 2 pour les gardiens et 1 pour le mensonge
circ = QuantumCircuit(3)

# Ajout d'une porte Hadamard pour mettre le trésor en superposition
circ.h(0)

# Ajout d'une porte CNOT pour intriquer les deux qbits des gardiens
circ.cx(0, 1)

# Ajout d'une autre porte Hadamard sur le qbit du mensonge
circ.h(2)

# Parcours du mensonge
circ.cx(2, 1)
circ.x(2)  # Pas besoin de spécifier "not", cela sert à appliquer une porte X
circ.cx(2, 0)
circ.x(2)

# Question : Quel gardien l'autre gardien me dira de prendre ?
circ.swap(0, 1)

# Réponse du mensonge
circ.x(0)
circ.x(1)

# Parcours du mensonge pour répondre à la question
circ.cx(2, 1)
circ.x(2)
circ.cx(2, 0)
circ.x(2)

# Mesure des qbits
circ.measure_all()

# Affichage du circuit
circ.draw("mpl")

# Utilisation d'un simulateur
simulator = Aer.get_backend('aer_simulator')
circ = transpile(circ, simulator)
result = simulator.run(circ).result()
counts = result.get_counts(circ)

# Affichage de l'histogramme des résultats
plot_histogram(counts, title='Enigme de la Porte des Tresors')

os.makedirs("TP1", exist_ok=True)
filename = "TP1/histogramme_tresor.png"
plt.savefig(filename)
print(f"Histogramme sauvegardé dans {filename}")

# Forcer l'affichage du graphique
plt.show()
