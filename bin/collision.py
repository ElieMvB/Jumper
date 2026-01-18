def collision(p1_x, p1_y, p1_longueur, p1_hauteur, p2_x, p2_y, p2_longueur, p2_hauteur):
    '''
    entrée:
    coordonnées et tailles de deux zones
    sortie:
    True si les eux zones se touchent
    '''
    if p1_x < p2_x + p2_longueur and p1_x + p1_longueur > p2_x and p1_y < p2_y + p2_hauteur and p1_y + p1_hauteur > p2_y:
        return True
    return False
