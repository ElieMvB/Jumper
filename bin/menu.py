import pyxel
from bin.jeux import*

class Menu:
    def __init__(self):
        #liste niveaux réussis
        self.liste_reussi = []
        #gère l'état du jeuxx (menu, encours...)
        self.etat = 'menu'
        #liste des niveaux
        self.niveaux = [
            {'init' : {'perso' : [30, 30], 'fond' : 1, 'plateformes' : [[20, 80, 20, 3, 9, 13, [0, 0]], [85, 80, 20, 3, 9, 13, [0, 0]],
                                                            [53, 70, 20, 3, 9, 13, [0, 0]], [-60, 40, 30, 3, 11, 13, [0.5, 0]]]
            },
            '8' : [['tpc', [-49, 25, -1, 0, 8, [1, 1], [2, 2]]], True],
            '20' : [['tpf', [-49, 25, -1, 0, 8, [1, 1], [2, 2]]], True],
            '45' : [['d', 3, [-3, 0]], True],
            '50' : [['d', 3, [0, 0]], True],
            '56' : [['tpc', [0, 128, -1, 0, 8, [0, 1.5], [2, 2]]], True],
            '65' : [['tpf', [0, 128, -1, 0, 8, [0, 1.5], [2, 2]]], True],
            '68' : [['d', 3, [0, -2]], True],
            '70' : [['t', 3, 48, 130], ['d', 3, [0, -2]], True],
            '72' : [['d', 3, [0, 0]], ['d', 2, [0, -1.5]], True],
            '75' : [['tpc', [0, 128, 128, 129, 8, [0, -1.5], [2, 2]]], True],
            '84' : [['tpf', [0, 128, 128, 129, 8, [0, -1.5], [2, 2]]], True],
            '96' : [['fin'], True]
            },
            
            {'init' : {'perso' : [30, 30], 'fond' : 1, 'plateformes' : [[20, 80, 20, 3, 9, 13, [0, 0]], [85, 80, 20, 3, 9, 13, [0, 0]],
                                                                [53, 70, 20, 3, 9, 13, [0, 0]], [-60, 40, 30, 3, 11, 13, [0, 0]]]
            },
             '5' : [['tpc', [0, 50, 0, 1, 8, [0, 1], [2, 2]]], ['tpc', [80, 128, 0, 1, 8, [0, 1], [2, 2]]], True],
             '15' : [['tpf', [0, 50, 0, 1, 8, [0, 1], [2, 2]]], ['tpf', [80, 128, 0, 1, 8, [0, 1], [2, 2]]], True],
             '25' : [['c', 2, 8], True],
             '30' : [['d', 2, [0, -2]], ['c', 1, 8], True],
             '35' : [['d', 1, [-1, 1]], True],
             '38' : [['d', 1, [0, 0]], ['c', 1, 9], ['tpc', [128, 129, 50, 100, 8, [-1, 0], [2, 2]]], True],
             '45' : [['tpf', [128, 129, 50, 100, 8, [-1, 0], [2, 2]]], True],
             '60' : [['t', 0, 53, 90], ['t', 2, 50, 70], ['d', 2, [0, 0]], ['c', 2, 9], True],
             '65' : [['c', 1, 8], True],
             '70' : [['c', 0, 8], ['t', 1, 129, 129], True],
             '75' : [['c', 2, 11], ['t', 0, 129, 129], True],
             '81' : [['fin'], True]
            },
            
            {'init' : {'perso' : [64, 4], 'fond' : 1, 'plateformes' : [
                                                            [20, 80, 20, 3, 1, 6, [0, 0]], [85,  80,  20, 3, 1, 6, [0, 0]],
                                                            [53, 20, 20, 3, 1, 6, [0, 0]], [53, 100, 20, 3, 1, 6, [0, 0]],
                                                            [20, 40, 20, 3, 1, 6, [0, 0]], [85,  40,  20, 3, 1, 6, [0, 0]],
                                                            [53, 60, 20, 3, 1, 6, [0, 0]], [3, 2, 4, 30, 1, 12, [0, 0]]
                                                            ]
            },
             
            '2' : [['tpc', [-5, 0, 0, 128, 8, [1, 0], [2, 2]]], True],
            '4' : [['d', 7, [0, 0.5]], True],
            '16' : [['d', 7, [0, -0.5]], True],
            '28' : [['d', 7, [0, 0.5]], True],
            '45' : [['tpf', [-5, 0, 0, 128, 8, [1, 0], [2, 2]]], True],
            '54' : [['t', 7, 120, -40], True],
            '59' : [['tpc', [128, 129, 0, 128, 8, [-1, 0], [2, 2]]], True],
            '80' : [['tpf', [128, 129, 0, 128, 8, [-1, 0], [2, 2]]], True],
            '90' : [['fin'], True]
            
            },
            
            {'init' : {'perso' : [30, 30], 'fond' : 1, 'plateformes' : [[20, 80, 20, 3, 11, 3 , [0, 0]],
                                                                        [100, 120, 20, 3, 11, 3, [0, 0]],
                                                                        [-30, 70, 20, 3, 9, 10, [0, 0]],
                                                                        [120, -40, 3, 30, 9, 13, [0, 0]],
                                                                        [-45, 100, 40, 3, 9, 10 , [0, 0]],
                                                                        [120, -30, 4, 30, 9, 10 , [0, 0]],
                                                                        [-35, 120, 30, 3, 12, 0, [0, 0]],
                                                                        ]
            },
             '3': [['d', 2, [1, 0]], True],
             '8' : [['tpc', [-2, 2, 0, 110, 8, [1, 0], [2, 2]]], True],
             '15' : [['tpf', [-2, 2, 0, 110, 8, [1, 0], [2, 2]]], True],
             '20' : [['d', 4, [1, 0]], True],
             '21' : [['d', 5, [0, 1]], True],
             '26' : [['tpc', [128, 130, 0, 130, 8, [-1, 0], [2, 2]]], True],
             '30' : [['tpf', [128, 130, 0, 130, 8, [-1, 0], [2, 2]]], True],
             '35' : [['d', 6, [1, 0]], True],
             '36' : [['tpc', [-2, 72, -1, 0, 8, [0, 1], [2, 2]]], True],
             '53' : [['tpf', [-2, 72, -1, 0, 8, [0, 1], [2, 2]]], True],   
             '72' : [['fin'], True]
            }
            ]
        
        #indique niveau sélectioné
        self.indexe = 0
        
        #il faut le niveau sélectionné en paramètre
        self.jeux = None
        
    def rafraichissement(self):
        if self.etat == 'menu':
            if pyxel.btnr(pyxel.KEY_SPACE): #lance le jeux
                self.etat = 'jeux'
                #initialise le jeuxx
                self.jeux = Jeux(self.niveaux[self.indexe])
            #déplace la sélection du niveau
            if pyxel.btnr(pyxel.KEY_UP):
                self.indexe -= 6
            elif pyxel.btnr(pyxel.KEY_DOWN):
                self.indexe += 6
            elif pyxel.btnr(pyxel.KEY_RIGHT):
                self.indexe += 1
            elif pyxel.btnr(pyxel.KEY_LEFT):
                self.indexe -= 1
            #vérification d'être bien sur la liste des niveaux
            if self.indexe >= len(self.niveaux):
                    self.indexe = len(self.niveaux) - 1
            elif self.indexe <= 0:
                self.indexe = 0

        if self.etat == 'jeux':
            #fait tourner le jeuxx
            self.jeux.rafraichissement()
            
            #vérifie conditions victoire/défaite
            if self.jeux.game_over == 2: #victoire
                self.etat = 'menu'
                pyxel.play(0, 0)
                for k in self.jeux.clefs:
                    if k != 'init': self.niveaux[self.indexe][k][-1] = True
                self.liste_reussi.append(self.indexe)
            elif self.jeux.game_over == 1: #défaite
                self.etat = 'menu'
                for k in self.jeux.clefs:
                    if k != 'init': self.niveaux[self.indexe][k][-1] = True
    
    def affiche(self):
        #affiche tout
        pyxel.cls(1)
        if self.etat == 'menu':
            pyxel.text(50, 20, "JUMPER!", 10)
            pyxel.blt(55, 30, 0, 24, 32, 16, 8, 2)
            pyxel.blt(59, 40, 0, 24, 24, 8, 8, 2)
            #affichage menu
            i = 0
            j = 0
            for n in self.niveaux:
                pyxel.rect(30 + 20 * i, 75 + 20 * j, 10, 10, 0)
                if self.indexe == self.niveaux.index(n):
                    pyxel.text(33 + 20 * i, 78 + 20 * j, str(self.niveaux.index(n) + 1), 11)
                else:
                    pyxel.text(33 + 20 * i, 78 + 20 * j, str(self.niveaux.index(n) + 1), 8)
                if self.niveaux.index(n) in self.liste_reussi:
                    pyxel.rectb(30 + 20 * i, 75 + 20 * j, 10, 10, 3)
                    pyxel.rectb(28 + 20 * i, 73 + 20 * j, 14, 14, 3)
                else:
                    pyxel.rectb(30 + 20 * i, 75 + 20 * j, 10, 10, 8)
                i += 1
                if i >= 6:
                    i = 0
                    j += 1
            pyxel.text(30, 100, 'appuyez sur espace', 7)
        if self.etat == 'jeux':
            #affichage jeuxx
            self.jeux.affiche()
