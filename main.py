from PIL import Image, ImageDraw
import numpy as np

import scene
import camera
import sphere

if __name__ == "__main__":
    # Création d'une caméra
    cam = camera.Camera(dimensions=(700, 500), position=np.array([0, 0, 10]), direction=np.array([0, 0, 1]), orientation=np.array([0, 1, 0]), distance_focale=1.0)

    # Création d'une image
    image = Image.new("RGB", (700, 500), "white")

    sphere1 = sphere.Sphere(10, np.array([10, 10, 0]))

    sphere1.dessiner_sphere(image)

    # Création d'une scène
    my_scene = scene.Scene(cam, image)

    # Ajout de la caméra à la scène (bien que cela soit redondant ici)
    my_scene.ajouter_camera(cam)

    image.show()

"""
    #AJOUT DE LA SCENE
    ajouter_scene()

    #AJOUT DES OBJETS
    ajouter_objets()

    #AJOUT SOURCE LUMINEUSE
    ajouter_lumieres()
"""
