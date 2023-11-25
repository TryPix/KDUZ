"""
Fonctions utiles pour un jeu de labyrinthe sur curses.
@ Maxime Lehmann
@ Saimaneesh Yeturu
"""
import curses
import time

def OpenAndPrepare(fichier):
    """Ouvrir un fichier et le préparer à l'impression dans curses."""
    lines = []
    with open(fichier) as fichier:
        content = fichier.readlines()
    for line in content:
        ligne = line.rstrip('\n')
        lines.append(ligne)
    return lines


def PleinEcran(cols, rows):
    """Forcer le plein écran."""
    while True: # vérifie la taille du terminal jusqu'à qu'il soit assez grand
        ecran = curses.initscr()
        curses.curs_set(0)
        num_rows, num_cols = ecran.getmaxyx()
        ecran.addstr(0, 0, FULL_SCREEN)
        curses.napms(200) # attendre un peu
        if num_cols > cols and num_rows > rows:
            ecran.clear()
            curses.endwin()
            break
        else:
            curses.endwin()


def Afficher(ecran, liste_lignes, x, y, color):
    """Afficher un objet."""
    for l in range(len(liste_lignes)):
        ligne = liste_lignes[l]
        for c in range(len(ligne)):
            ecran.addch(y + l, x + c, ligne[c], curses.color_pair(color)) # set inital position


def Effacer(ecran, objet_a_effacer, x, y):
    """Effacer un objet. En réalité juste afficher des espaces."""
    for line in range(len(objet_a_effacer)): # remove previous
        ligne = " " * len(objet_a_effacer[line])
        for c in range(len(ligne)):
            ecran.addch(y + line, x + c, " ")


def AllPositions(object, x, y):
    """Trouve toutes les positions occupées par un objet."""
    xy = []
    for l in range(len(object)):
        ligne = object[l]
        for c in range(len(ligne)):
            if ligne[c] != " ":
                xy.append((y+l, x+c))
    return xy


def IsSuperposed(allpositions1, allpositions2):
    """Vérifie si deux objets sont en superposition."""
    for i in range(len(allpositions1)):
        for j in range(len(allpositions2)):
            if allpositions1[i] == allpositions2[j]:
                return True
    return False


def NewPos(ecran, x1, y1, player, x2, y2, object, touche, displacement=2):
    """
    Détermine la nouvelle position du héros, dans un tuple.
    La position est seulement possible si la nouvelle position du joueur ne
    rentre pas en collision avec un objet. La vitesse de deplacement est fixée
    à deux car il est difficile de gérer toutes les possibilités pour des
    valeurs supérieures. S'il n'est pas possible de se déplacer de deux places,
    le héros se déplacera de 1.
    """
    POS_OBJ = AllPositions(object, x2, y2)
    old_pos = (x1, y1)
    if touche == ord("w"):
        if not IsSuperposed(AllPositions(player, x1, y1 - displacement),
                            POS_OBJ):
            y1 -= displacement
        elif not IsSuperposed(AllPositions(player, x1, y1 - (displacement-1)),
                            POS_OBJ):
            y1 -= (displacement - 1)
    if touche == ord("s"):
        if not IsSuperposed(AllPositions(player, x1, y1 + displacement),
                            POS_OBJ):
            y1 += displacement
        elif not IsSuperposed(AllPositions(player, x1, y1 + (displacement-1)),
                            POS_OBJ):
            y1 += (displacement - 1)
    if touche == ord("d"):
        if not IsSuperposed(AllPositions(player, x1 + displacement, y1),
                            POS_OBJ):
            x1 += displacement
        elif not IsSuperposed(AllPositions(player, x1 + (displacement-1), y1),
                            POS_OBJ):
            x1 += (displacement - 1)
    if touche == ord("a"):
        if not IsSuperposed(AllPositions(player, x1 - displacement, y1),
                            POS_OBJ):
            x1 -= displacement
        elif not IsSuperposed(AllPositions(player, x1 - (displacement-1), y1),
                            POS_OBJ):
            x1 -= (displacement - 1)
    return (x1, y1)


def Center(ecran, object, decal_y, num_rows, num_cols, decal_x=0):
    """Centrer un objet dans curses."""
    center_point = (num_rows/2, num_cols/2)
    positions = AllPositions(object, 0, 0)
    x = []
    y = []
    for coordinate in positions:
        y.append(coordinate[0])
        x.append(coordinate[1])
    x_max = max(x)
    y_max = max(y)
    y_start = center_point[0] - y_max/2
    x_start = center_point[1] - x_max/2
    return int(y_start) + decal_y, int(x_start) + decal_x


