# Visualisation 3D du Genou et Détection du Point d’Isométrie du LCA – Projet de Stage 

Ce projet s’inscrit dans le cadre d’un stage de **Licence Informatique** au sein du laboratoire **MIS – UPJV**.

Il a pour objectif le développement d’un outil interactif permettant la **visualisation 3D du genou** ainsi que l’**intégration d’une méthode de détection du point d’isométrie** du ligament croisé antérieur (LCA), à partir de fichiers STL issus d’imageries ou de simulations biomécaniques.

---

## Objectifs actuels

### Tâche 1 – Lecture, segmentation et affichage
- Charger un fichier `.stl` contenant les trois os du genou (fémur, rotule, tibia), pour différentes positions (angles de flexion).
- Segmenter automatiquement les os à partir de leur connectivité et de leur position spatiale.
- Identifier chaque volume à l’aide de critères anatomiques :
  - **Rotule** : plus petit volume,
  - **Tibia** : situé le plus bas (coordonnée Z),
  - **Fémur** : situé le plus haut (coordonnée Z).
- Afficher les volumes 3D avec des couleurs distinctes.
- Permettre le masquage/affichage individuel des os via des cases à cocher dans l’interface.

### Tâche 2 – Interaction (en cours)
- [x] Référentiel 3D (axes orientés X, Y, Z) : déjà intégré via `plotter.add_axes()`.
- [ ] Positionnement manuel d’une sphère sur un os sélectionné.
- [ ] Affichage dynamique des coordonnées de la sphère (X, Y, Z).

---

## Structure du projet

```
isoLCA/
│
├── stl_files/          → Fichiers STL à analyser
│   ├── 1.stl
│   ├── 2.stl
│   └── ...
│
├── src/                → Code source
│   ├── stl_loader.py   # Chargement & segmentation STL
│   ├── viewer.py       # Affichage interactif 3D
│
├── main.py             → Script principal
├── requirements.txt    → Dépendances à installer
└── README.md           → Ce fichier
```

---

## Lancement de l'application

### 1. Cloner le dépôt

```
git clone <lien-du-repo>
cd isoLCA
```

### 2. Créer et activer l’environnement Conda

```
conda create -n stl-viewer python=3.10
conda activate stl-viewer
```

### 3. Installer les dépendances

```
pip install -r requirements.txt
```

### 4. Lancer l'application

```
python main.py
```
---

## Réalisé par

- **Mohamed Amine Sobhi**  
  Stagiaire – Avril 2025  
---

## Collaborations

Ce dépôt est partagé avec :
- **Monsieur Gilles Dequen**, maître de stage, pour le suivi technique et la validation.

---
