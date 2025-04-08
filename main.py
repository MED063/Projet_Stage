from PyQt5.QtWidgets import QApplication, QFileDialog
from src.stl_loader import charger_et_segmenter
from src.viewer import afficher_os
import os

app = QApplication([])

def choisir_fichier(dossier="stl_files"):
    return QFileDialog.getOpenFileName(None, "Sélectionnez un fichier STL", dossier, "Fichiers STL (*.stl)")[0]

if __name__ == "__main__":
    print(" Visualiseur 3D – Modèles de genou")

    while True:
        fichier = choisir_fichier()
        if not fichier:
            print(" Aucun fichier sélectionné.")
            break

        volumes = charger_et_segmenter(fichier)
        if volumes:
            afficher_os(volumes, nom_fichier=os.path.basename(fichier))
        else:
            print(" Aucun os détecté dans ce fichier.")

        if input("\nEntrée ⏎ = nouveau fichier | q = quitter : ").lower().strip() == "q":
            break
            