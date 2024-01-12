import os
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def init_circ():
    circ = QuantumCircuit(2)
    circ.h(0)
    circ.h(1)
    circ.barrier()
    return circ

def oracle_grimoire_1(circ):
    circ.x(0)
    circ.x(1)
    circ.cz(0, 1)
    circ.x(0)
    circ.x(1)
    circ.barrier()

def oracle_grimoire_2(circ):
    circ.x(1)
    circ.cz(0, 1)
    circ.x(1)
    circ.barrier()

def oracle_grimoire_3(circ):
    circ.x(0)
    circ.cz(0, 1)
    circ.x(0)
    circ.barrier()

def oracle_grimoire_4(circ):
    circ.cz(0, 1)
    circ.barrier()

def diffuseur(circ):
    circ.h(0)
    circ.h(1)
    circ.z(0)
    circ.z(1)
    circ.cz(0,1)
    circ.h(0)
    circ.h(1)
    circ.barrier()

def build_circ(grimoire):
    circ = init_circ()

    if grimoire == 1:
        oracle_grimoire_1(circ)
    elif grimoire == 2:
        oracle_grimoire_2(circ)
    elif grimoire == 3:
        oracle_grimoire_3(circ)
    elif grimoire == 4:
        oracle_grimoire_4(circ)
    else:
        raise ValueError("grimoire should be between 1 and 4")

    diffuseur(circ)
    return circ

def simulate(circ):
    circ.measure_all()
    
    simulator: AerSimulator = Aer.get_backend('aer_simulator')
    circ = transpile(circ, simulator)
    result = simulator.run(circ).result()
    counts = result.get_counts(circ)

    return counts

# Fonction pour sauvegarder la figure
def save_figure(circ, grimoire):
    # Créer le dossier TP3 s'il n'existe pas déjà
    os.makedirs("TP3", exist_ok=True)

    # Enregistrer la figure dans le dossier TP3
    circuit_filename = f"TP3/grimoire_{grimoire}_circuit.png"
    circ.draw("mpl", style="clifford", filename=circuit_filename)
    print(f"Figure pour le Grimoire n°{grimoire} enregistrée dans {circuit_filename}")

    # Enregistrer l'histogramme dans le dossier TP3
    counts = simulate(circ)
    histogram_filename = f"TP3/grimoire_{grimoire}_histogram.png"
    plot_histogram(counts, title=f"Répartition des résultats pour le grimoire {grimoire}").savefig(histogram_filename)
    print(f"Histogramme pour le Grimoire n°{grimoire} enregistré dans {histogram_filename}")

# Test pour chaque grimoire
for grimoire in range(1, 5):
    circ = build_circ(grimoire)

    print(f"\nGrimoire n°{grimoire}\n")
    save_figure(circ, grimoire)

# Afficher toutes les figures à la fin
plt.show()
