# viewer.py – Affichage interactif 3D + mesures 

import pyvista as pv
from typing import Dict, Optional, Union
import numpy as np
import time

class MeasurementHandler:
    """Classe pour gérer plusieurs mesures sur la scène."""
    def __init__(self, plotter):
        self.plotter = plotter
        self.measurements = []  # Stocke un dict pour chaque mesure
        self.current_points = []  # Points pour la mesure en cours

    def add_point(self, point):
        self.current_points.append(point)
        sphere = pv.Sphere(radius=2, center=point)
        sphere_actor = self.plotter.add_mesh(sphere, color="yellow", name=f"sphere_{len(self.current_points)}")
        return sphere_actor

    def complete_measurement(self):
        if len(self.current_points) != 2:
            return
        p1, p2 = np.array(self.current_points[0]), np.array(self.current_points[1])
        dist = np.linalg.norm(p2 - p1)
        measurement_name = f"mesure_{len(self.measurements)+1}"
        line = pv.Line(p1, p2)
        line_actor = self.plotter.add_mesh(line, color="black", line_width=4, name=measurement_name)
        # Calculer le point médian pour le label
        midpoint = (p1 + p2) / 2
        label_text = f"{measurement_name}: {dist:.2f} mm"
        label_actor = self.plotter.add_point_labels(
            [midpoint], [label_text],
            name=f"label_{measurement_name}",
            text_color="black",
            font_size=20,
            shadow=True,
            background_color="white",
            background_opacity=0.6
        )

        # Stocker la mesure
        self.measurements.append({
            "name": measurement_name,
            "distance": dist,
            "line_actor": line_actor,
            "label_actor": label_actor
        })
        # Effacer la mesure en cours
        self.current_points = []
        
    def reset_current(self):
        self.current_points.clear()

def afficher_os(os_segmentes: Dict[str, Union[pv.DataSet, None]], nom_fichier: Optional[str] = None) -> None:
    plotter = pv.Plotter(window_size=[1400, 1000])

    # Définition de l'ordre, des couleurs et des labels pour les os
    ordre_os = ["femur", "rotule", "tibia"]
    couleurs = {"femur": "red", "rotule": "green", "tibia": "blue"}
    labels = {"femur": "Fémur", "rotule": "Rotule", "tibia": "Tibia"}
    
    meshes_visibles = {nom: True for nom in ordre_os}

    for nom in ordre_os:
        mesh = os_segmentes.get(nom)
        if mesh is None:
            continue
        mesh = mesh.extract_surface() if not isinstance(mesh, pv.PolyData) else mesh
        plotter.add_mesh(mesh, name=nom, color=couleurs[nom], pickable=True)
        plotter.add_point_labels(
            [mesh.center], [labels[nom]],
            name=f"label3d_{nom}",
            text_color=couleurs[nom],
            font_size=14,
            shadow=True
        )

    def toggle_actor(nom: str, is_visible: bool) -> None:
        meshes_visibles[nom] = is_visible
        acteur = plotter.renderer._actors.get(nom)
        label3d = plotter.renderer._actors.get(f"label3d_{nom}")
        if acteur:
            acteur.SetVisibility(is_visible)
        if label3d:
            label3d.SetVisibility(is_visible)
        plotter.render()

    def make_toggle(nom: str):
        return lambda val: toggle_actor(nom, val)

    if nom_fichier:
        plotter.add_text(
            f"Fichier : {nom_fichier}",
            position=(20, plotter.window_size[1] - 30),
            font_size=12,
            color="black",
            shadow=True
        )

    plotter.add_text(
        "Coordonnées du point: Cliquez sur un os",
        position=(20, 40),
        font_size=12,
        color="black",
        shadow=True,
        name="coord_display"
    )

    # Initialisation du gestionnaire de mesures
    meas_handler = MeasurementHandler(plotter)

    # Callback du picking sur la surface (seuls les clics sur les maillages/volumes déclenchent le callback)
    def update_measurement(point):
        if point is None:
            print("⚠ Aucun point sélectionné sur un os.")
            return
        # On ajoute le point courant et on met à jour la zone des coordonnées
        meas_handler.add_point(point)
        coord_str = f"Coordonnées du point: X={point[0]:.2f}, Y={point[1]:.2f}, Z={point[2]:.2f}"
        plotter.add_text(
            coord_str,
            position=(20, 40),
            font_size=12,
            color="black",
            shadow=True,
            name="coord_display",
            render=True
        )
        # Si deux points ont été récupérés, compléter la mesure
        if len(meas_handler.current_points) == 2:
            meas_handler.complete_measurement()

    plotter.enable_surface_point_picking(
        callback=update_measurement,
        pickable_window=False,
        left_clicking=True,
        tolerance=0.001,
        show_message=False
    )

    margin_top, start_x_checkbox, start_x_label, step_y = 80, 20, 60, 40
    for i, nom in enumerate(ordre_os):
        pos_y = plotter.window_size[1] - (margin_top + i * step_y)
        plotter.add_checkbox_button_widget(
            make_toggle(nom),
            position=(start_x_checkbox, pos_y),
            size=20,
            value=True,
            color_on="green",
            color_off="red"
        )
        plotter.add_text(
            labels[nom],
            position=(start_x_label, pos_y),
            font_size=12,
            viewport=False,
            shadow=True,
            color=couleurs[nom]
        )

    plotter.view_isometric()
    plotter.background_color = "white"
    plotter.add_axes()
    plotter.show()
