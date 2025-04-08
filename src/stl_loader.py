# stl_loader.py – Chargement et segmentation  des os depuis un fichier STL
import pyvista as pv
import numpy as np

def charger_et_segmenter(filepath):
    """Charge un fichier STL et segmente les os (rotule, tibia, fémur) selon leur taille et position Z."""
    try:
        mesh = pv.read(filepath)
    except Exception as e:
        print(f"[Erreur] Chargement STL : {e}")
        return {}

    # Séparation les régions non connectées ( les 3 os)
    labeled = mesh.connectivity(mode='points', output_values='point_arrays')
    n_regions = int(labeled['RegionId'].max() + 1)
    print(f"[Info] Régions détectées : {n_regions}")
    if n_regions < 3:
        print("[Alerte] Moins de 3 régions détectées.")
        return {}

    # Extraction de  chaque région + calculs  (nb points, hauteur moyenne)
    infos = []
    for i in range(n_regions):
        r = labeled.threshold([i, i], scalars='RegionId')
        infos.append({
            'region': r,
            'n_points': r.n_points,
            'z_mean': np.mean(r.points[:, 2])
        })

    # Identification des volumes/os :
    # - la rotule = plus petit volume
    # - le tibia = plus bas (Z)
    # - le fémur = plus haut (Z)
    infos.sort(key=lambda r: r['n_points'])  # rotule = plus petit
    os_segmentes = {
        'rotule': infos[0]['region'],
        'tibia':  min(infos[1:], key=lambda r: r['z_mean'])['region'],
        'femur':  max(infos[1:], key=lambda r: r['z_mean'])['region']
    }

    print(f"[Info] Os segmentés : ['rotule', 'femur', 'tibia']")
    print(f"[Détail] Points : Rotule={infos[0]['n_points']}, "
          f"Tibia={min(infos[1:], key=lambda r: r['z_mean'])['n_points']}, "
          f"Fémur={max(infos[1:], key=lambda r: r['z_mean'])['n_points']}")

    return os_segmentes
