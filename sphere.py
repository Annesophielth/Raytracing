from PIL import Image, ImageDraw
import numpy as np


class Sphere:
    def __init__(self, rayon, centre):
            self.rayon = rayon
            self.centre = centre
            self.pixel = []



    def renvoie_centre(self):
      res = []
      res.append(self.centre[0])
      res.append(self.centre[1])
      res.append(self.centre[2])

      return res


    def dessiner_sphere(self, image, couleur=(1, 0, 0), epaisseur=1):
        



        draw = ImageDraw.Draw(image)
        x0, y0 = self.centre[0] - self.rayon, self.centre[1] - self.rayon
        x1, y1 = self.centre[0] + self.rayon, self.centre[1] + self.rayon
        draw.ellipse([x0, y0, x1, y1], outline=couleur, width=epaisseur)



    def intersection(self, rayon_vue, origine):


      a = np.dot(rayon_vue, rayon_vue) #qui doit etre égal à 1 si normalisé
      b = 2 * np.dot(origine - self.centre)
      c = np.dot((origine - self.centre), (origine - self.centre))    - self.rayon * self.rayon


      delta = (b*b) - 4 * a * c



      if delta == 0:
        """
        PARTIE TANGEANTE
        """
        return - b / (2 * a)


      elif delta > 0:
        t1 = (-b + math.sqrt(delta)) / (2 * a)
        t2 = (-b - math.sqrt(delta)) / (2 * a)

        return t1, t2

      else:
        return None
