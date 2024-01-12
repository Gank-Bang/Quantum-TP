from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os

def solve_hair_color_enigma():
    # Création du circuit avec 8 qubits
    circ = QuantumCircuit(8)

    # Portes Hadamard pour créer des superpositions de couleurs de cheveux possibles
    for i in range(4):
        circ.h(i)
    
    circ.barrier()

    # Alice utilise des portes CNOT pour calculer le nombre de chevelures indigo devant elle
    circ.cx(4, 1)
    circ.cx(4, 2)
    circ.cx(4, 3)
    
    circ.barrier()

    # Bob, Charlie et Dalia enregistrent le résultat dans leurs qubits de raisonnement
    for i in range(3):
        circ.cx(4, 5 + i)
    
    circ.barrier()

    # Bob utilise des portes CNOT pour déduire la couleur de ses cheveux
    circ.cx(2, 5)
    circ.cx(3, 5)
    
    circ.barrier()

    # Charlie et Dalia prennent note de la réponse de Bob
    for i in range(2):
        circ.cx(5, 6 + i)
    
    circ.barrier()

    # Charlie note la couleur de la chevelure devant lui
    circ.cx(3, 6)
    
    circ.barrier()

    # Dalia note la réponse et annonce la couleur
    circ.cx(6, 7)

    # Mesure des qubits
    circ.measure_all()

    # Simulation
    simulator = Aer.get_backend('aer_simulator')
    circ = transpile(circ, simulator)
    result = simulator.run(circ, shots=100_000).result()
    counts = result.get_counts(circ)

    # Affichage de l'histogramme des résultats
    plot_histogram(counts, title='Répartition des couleurs de cheveux')



# Exécution de la simulation
solve_hair_color_enigma()

os.makedirs("TP2", exist_ok=True)
filename = "TP2/histrogramme_repartition_cheveux"
plt.savefig(filename)
print(f"Histogramme sauvegardé dans {filename}")

plt.show()
