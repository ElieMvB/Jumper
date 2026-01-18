class Plateforme:
    #objets plateforme
    def __init__(self, x, y, longueur, hauteur, couleur, couleur_bordure, deplacement):
        self.x = x
        self.y = y
        self.longueur = longueur
        self.hauteur = hauteur
        self.couleur = couleur
        self.couleur_bordure = couleur_bordure
        self.deplacement = deplacement
            
    
    def mouvement(self):
        #déplace la palteforme
        self.x += self.deplacement[0]
        self.y += self.deplacement[1]
        
    
    def teleportation(self, x, y):
        #place a des coordonnées (x,y) la plateforme
        self.x = x
        self.y = y
