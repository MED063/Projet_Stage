# Visualisation 3D du Genou et Détection du Point d’Isométrie du LCA – Projet de Stage 

Ce projet s’inscrit dans le cadre de mon stage de **Licence 3 Informatique** au sein du laboratoire **MIS – UPJV**.

Il a pour objectif le développement d’un outil interactif permettant la **visualisation 3D du genou** ainsi que l’**intégration d’une méthode de détection du point d’isométrie** du ligament croisé antérieur (LCA).

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

### Tâche 2 – Interaction utilisateur
- [x] Référentiel 3D (axes orientés X, Y, Z), ajouté via `plotter.add_axes()`.
- [x] Positionnement manuel d’une sphère sur un os avec clic souris.
- [x] Affichage dynamique des coordonnées du point sélectionné (X, Y, Z) dans la scène.

### Tâche 3 – Mesure de distance entre deux points
- Ajout d’un outil de mesure interactif permettant de calculer la **distance euclidienne entre deux points** placés par l’utilisateur sur les surfaces osseuses.
- Chaque mesure affiche automatiquement :
  - Une ligne noire entre les deux points sélectionnés,
  - Une **étiquette au centre** affichant la distance calculée avec deux décimales (ex : `13.67 mm`).
- L’étiquette est mise en valeur avec une taille de police agrandie (`font_size=20`) et un **fond blanc semi-transparent** pour une meilleure lisibilité (`background_color="white"`, `background_opacity=0.6`).
- Les distances peuvent être mesurées :
  - Entre deux points du **même os**,
  - Ou entre deux points situés sur **des os différents**.
- Plusieurs mesures successives sont possibles, toutes étant conservées et nommées automatiquement (`mesure_1`, `mesure_2`, etc.).

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
│   ├── viewer.py       # Affichage interactif 3D + mesures 
│
├── main.py             → Script principal
├── requirements.txt    → Dépendances à installer
└── README.md           → Ce fichier
```

---

## Lancement de l'application

### 1. Cloner le dépôt

```
git clone https://github.com/MED063/isoLCA.git
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

##  Rapport de stage ( en cours )

 [Télécharger la version actuelle en PDF](https://github.com/MED063/isoLCA/blob/main/lca_prototype_rpprt.pdf)


## Réalisé par

- **Mohamed Amine Sobhi**  
  Stagiaire   
---

## Collaborations

Ce dépôt est partagé avec :
- **Monsieur Gilles Dequen**, maître de stage, pour le suivi technique et la validation.

---
