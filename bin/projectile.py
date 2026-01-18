import pyxel

class Projectile:
    def __init__(self, x, y, couleur, mouvement, taille=[2,2]):
        self.x = x
        self.y = y
        self.longueur = taille[0]
        self.hauteur = taille[1]
        self.couleur = couleur
        self.mouvement = mouvement
        
    def deplace(self):
        self.x += self.mouvement[0]
        self.y += self.mouvement[1]
        
    def affiche(self):
        #affiche le projectile
        pyxel.rect(self.x, self.y, self.longueur, self.hauteur, self.couleur)

