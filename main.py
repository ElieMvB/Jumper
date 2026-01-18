import pyxel
from bin.menu import*

M = Menu()

pyxel.init(128, 128)
pyxel.load('ressources.pyxres')
pyxel.run(M.rafraichissement, M.affiche)