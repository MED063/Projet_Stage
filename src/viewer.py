# viewer.py – Affichage interactif des os segmentés avec PyVista
import pyvista as pv
from typing import Dict, Optional, Union

def afficher_os(os_segmentes: Dict[str, Union[pv.DataSet, None]], nom_fichier: Optional[str] = None) -> None:
    plotter = pv.Plotter(window_size=[1400, 1000])

    # Ordre d'affichage + configuration couleurs et labels
    ordre_os = ["femur", "rotule", "tibia"]
    couleurs = {"femur": "red", "rotule": "green", "tibia": "blue"}
    labels = {"femur": "Fémur", "rotule": "Rotule", "tibia": "Tibia"}

    # Ajout des volumes segmentés à la scène
    for nom in ordre_os:
        mesh = os_segmentes.get(nom)
        if mesh is None:
            continue
        mesh = mesh.extract_surface() if not isinstance(mesh, pv.PolyData) else mesh
        plotter.add_mesh(mesh, name=nom, color=couleurs[nom])
        plotter.add_point_labels(
            [mesh.center], [labels[nom]],
            name=f"label3d_{nom}",
            text_color=couleurs[nom],
            font_size=14,
            shadow=True
        )

    # Fonction de masquage/affichage des volumes + labels
    def toggle_actor(nom: str, is_visible: bool) -> None:
        acteur = plotter.renderer._actors.get(nom)
        label3d = plotter.renderer._actors.get(f"label3d_{nom}")
        if acteur:
            acteur.SetVisibility(is_visible)
        if label3d:
            label3d.SetVisibility(is_visible)
        plotter.render()

    def make_toggle(nom: str):
        return lambda val: toggle_actor(nom, val)

    #  nom du fichier selectionné 
    if nom_fichier:
        plotter.add_text(
            f"Fichier : {nom_fichier}",
            position=(20, plotter.window_size[1] - 30),
            font_size=12,
            color="black",
            shadow=True
        )

    # Cases à cocher + labels associés, positionnés en pixels
    margin_top, start_x_checkbox, start_x_label, step_y = 80, 20, 60, 40
    for i, nom in enumerate(ordre_os):
        pos_y = plotter.window_size[1] - (margin_top + i * step_y)

        # Checkbox toggle
        plotter.add_checkbox_button_widget(
            make_toggle(nom),
            position=(start_x_checkbox, pos_y),
            size=20,
            value=True,
            color_on="green",
            color_off="red"
        )

        # Texte à côté de la case
        plotter.add_text(
            labels[nom],
            position=(start_x_label, pos_y),
            font_size=12,
            viewport=False,
            shadow=True,
            color=couleurs[nom]
        )

    # Config finale de la scene
    plotter.view_isometric()
    plotter.background_color = "white"
    plotter.add_axes()
    plotter.show()
