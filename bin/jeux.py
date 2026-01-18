import pyxel
from random import randint
from bin.collision import*
from bin.plateforme import*
from bin.projectile import*

class Jeux:
    #objet du jeux
    def __init__(self, niveau=None):
        #initialisation des variables du joueur
       self.perso_x = 30
       self.perso_y = 30
       self.perso_anim = 0
       self.perso_dg = 1
       
       self.tomber = True
       self.memoire_saut = 0
       
       #initialisation listes
       self.plateformes = []
       self.liste_explosions = []
       self.liste_projectiles = []
       self.type_projectiles = []
       
       #initialisation quelques variables
       self.chrono = 0
       self.game_over = 0
       
       #initialisations des variables spécifiques au niveau
       self.niveau = niveau
       self.clefs = [k for k in niveau.keys()]
       for p in self.niveau['init']['plateformes']:
           self.plateformes.append(Plateforme(p[0], p[1], p[2], p[3], p[4], p[5], p[6]))
       self.perso_x = self.niveau['init']['perso'][0]
       self.perso_y = self.niveau['init']['perso'][1]
       self.temps = int(self.clefs[-1]) // 3
       self.couleur_fond = self.niveau['init']['fond']
        
       
       
    def saut(self):
        #gère la physique du perso
        for plat in self.plateformes:
            if self.perso_x + 7 > plat.x and self.perso_x < plat.x + plat.longueur and self.perso_y == plat.y - 8:
                self.tomber = False
                if pyxel.btn(pyxel.KEY_SPACE):
                    self.memoire_saut = 10
                    
        if self.tomber == True and self.memoire_saut == 0:
            self.perso_y += 2
                     
        if self.memoire_saut > 0 and self.tomber == False:
            self.perso_y -= 2
            self.memoire_saut -= 1               
        else:
            self.tomber = True
            
    def animation_perso(self):
        #gère vitesse animation perso
        if pyxel.frame_count % 25 == 0:
            self.perso_anim += 1
            if self.perso_anim >= 2:
                self.perso_anim = 0
            
        
    def deplacement_perso(self):
        #déplace le personnage
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.perso_x += 2
            self.perso_dg = 1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.perso_x -= 2
            self.perso_dg = 0
            
    def evenement(self):
        #lance les divers évènements du niveau par rapport au chrono
        if str(self.chrono) in self.clefs:
            e = self.niveau[str(self.chrono)]
            if e[-1]:
                for i in range(len(e)-1):
                    #conditions action...
                    if e[i][0] == 'd':
                        self.plateformes[e[i][1]].deplacement = e[i][2]
                    elif e[i][0] == 't':
                        self.plateformes[e[i][1]].x = e[i][2]
                        self.plateformes[e[i][1]].y = e[i][3]
                    elif e[i][0] == 'c':
                        self.plateformes[e[i][1]].couleur = e[i][2]
                    elif e[i][0] == 'tpc':
                        self.type_projectiles.append(e[i][1])
                    elif e[i][0] == 'tpf':
                        self.type_projectiles.remove(e[i][1])
                    elif e[i][0] == 'fin':
                        self.game_over = 2 #2 -> victoire
                    e[-1] = False #on met False pour que l'évènement ne se répète pas
            
    
    def rafraichissement(self):
        #mise a jour du jeuxx
        self.deplacement_perso()
        self.saut()
        self.animation_perso()
        
        #gère vitesse jeuxx
        if pyxel.frame_count % 10 == 0:
            self.chrono += 1
        if pyxel.frame_count % 30 == 0:
            self.temps -= 1
        
        #lance les évènements du niveau
        self.evenement()
            
        #création projectiles
        if pyxel.frame_count % 2 == 0:
            for t in self.type_projectiles:
                self.liste_projectiles.append(Projectile(randint(t[0], t[1]), randint(t[2], t[3]), t[4], t[5], t[6]))
        for p in self.liste_projectiles:
            p.deplace()
        for plat in self.plateformes:
            plat.mouvement()

        #collisions projectiles
        for project in self.liste_projectiles:
            for plat in self.plateformes:
                if collision(plat.x, plat.y, plat.longueur, plat.hauteur, project.x, project.y, project.longueur, project.hauteur):
                    self.liste_projectiles.remove(project)
                    self.liste_explosions.append([project.x, project.y, 0, 3, 8])
            if project.x < -50 or project.x > 160 or project.y < -50 or project.y > 160:
                self.liste_projectiles.remove(project)
            if collision(self.perso_x, self.perso_y, 8, 5, project.x, project.y, project.longueur, project.hauteur):
                self.game_over = 1
                if project in self.liste_projectiles:
                    self.liste_projectiles.remove(project)
        if self.perso_y >= 129:
            self.game_over = 1
            
        #animation explosions
        if pyxel.frame_count % 10:
            for exp in self.liste_explosions:
                exp[2] += 1
                if exp[2] > exp[3]:
                    self.liste_explosions.remove(exp)
        
        
    def affiche(self):
        #affiche les éléments de l'écran du jeuxx
        #fond (dépend du niveau)
        pyxel.rect(0, 0, 128, 128, self.couleur_fond)
        #joueur
        if (self.memoire_saut > 0):
            pyxel.blt(self.perso_x, self.perso_y, 0, 40, 8 * self.perso_dg, 8, 8, 2)
        else:
            pyxel.blt(self.perso_x, self.perso_y, 0, 24 + 8 * self.perso_anim, 8 * self.perso_dg, 8, 8, 2)
        
        #platefromes
        for plat in self.plateformes:
            pyxel.rect(plat.x, plat.y, plat.longueur, plat.hauteur, plat.couleur_bordure)
            pyxel.rect(plat.x+1, plat.y+1, plat.longueur-2, plat.hauteur-2, plat.couleur)
        
        #projectiles
        for proj in self.liste_projectiles:
            proj.affiche()
        
        #explosions
        for exp in self.liste_explosions:
            pyxel.circb(exp[0], exp[1], exp[2], exp[4])
        
        #temps
        pyxel.rect(108, 8, 10, 10, 7)
        pyxel.text(110, 10, str(self.temps), 0)
        pyxel.rectb(107, 7, 12, 11, 0)
            
