"""
kduz - un jeu d'aventure ou vous êtes un bonhomme de neige qui essaye de
reprendre les neige qui lui a été volé par les méchants Aaas7.

@ Maxime Lehmann and Saimaneesh Yeturu
CEC André-Chavanne
301bi
Classe OC python, M. Kessler

Sources:
https://docs.python.org/3/howto/curses.html
https://www.devdungeon.com/content/curses-programming-python

"""

import time
import os
import curses
import maze
import time
import sys
# python -m pip install windows-curses

BACKGROUND_FICH = "data/background.txt" # fichiers
HERO_FICH = "data/hero.txt"
HLF_DEAD_FICH = "data/hero_half_dead.txt"
DEAD_FICH = "data/hero_dead.txt"
NPC_FICH = "data/npc.txt"
LEVEL1_FICH = "data/level1.txt"
TOP_WIN_FICH = "data/top_window.txt"
HEART_FICH = "data/heart.txt"
KDUZ_FICH = "data/kduz_logo.txt"
M_JOUER_FICH = "data/menu_jouer.txt"
M_REGLES_FICH = "data/menu_regles.txt"
M_QUIT_FICH = "data/menu_quitter.txt"
LEVELM_FICH = "data/niveau1_menu.txt"
REGLES_FICH = "data/regles.txt"
G_OVER_FICH = "data/gameover.txt"
SMALL_LOGO_FICH = "data/kduz_petit.txt"
SHOOTER_FICH = "data/shooter.txt"
ARROW_FICH = "data/arrow.txt"
FLOCON_FICH = "data/flocon.txt"
VIC_FICH = "data/victory.txt"
COMIC_FICH = "data/comic.txt"
TOP_WIN_LINES = maze.OpenAndPrepare(TOP_WIN_FICH) # preparation des fichiers
HERO_LINES = maze.OpenAndPrepare(HERO_FICH)
HALF_DEAD = maze.OpenAndPrepare(HLF_DEAD_FICH)
DEAD = maze.OpenAndPrepare(DEAD_FICH)
LEVEL1_LINES = maze.OpenAndPrepare(LEVEL1_FICH)
NPC_LINES = maze.OpenAndPrepare(NPC_FICH)
HEART_LINES = maze.OpenAndPrepare(HEART_FICH)
KDUZ_LINES = maze.OpenAndPrepare(KDUZ_FICH)
M_JOUER_LINES = maze.OpenAndPrepare(M_JOUER_FICH)
M_REGLES_LINES = maze.OpenAndPrepare(M_REGLES_FICH)
M_QUIT_LINES = maze.OpenAndPrepare(M_QUIT_FICH)
UI_LEVEL1 = maze.OpenAndPrepare(LEVELM_FICH)[0:16]
UI_LEVEL2 = maze.OpenAndPrepare(LEVELM_FICH)[17:33]
UI_LEVEL3 = maze.OpenAndPrepare(LEVELM_FICH)[34:50]
REGLES = maze.OpenAndPrepare(REGLES_FICH)
GAME_OVER = maze.OpenAndPrepare(G_OVER_FICH)
SMALL_LOGO = maze.OpenAndPrepare(SMALL_LOGO_FICH)
SHOOTER = maze.OpenAndPrepare(SHOOTER_FICH)
ARROW = maze.OpenAndPrepare(ARROW_FICH)
FLOCON = maze.OpenAndPrepare(FLOCON_FICH)
VICTORY = maze.OpenAndPrepare(VIC_FICH)
COMIC1 = maze.OpenAndPrepare(COMIC_FICH)[0:18]
COMIC2 = maze.OpenAndPrepare(COMIC_FICH)[18:38]
COMIC3 = maze.OpenAndPrepare(COMIC_FICH)[38:55]
COMIC4 = maze.OpenAndPrepare(COMIC_FICH)[55:81]

WIDTH = 170 # taille des fenêtres
TOP_WIN_H = 12
BOT_WIN_H = 47
MAIN_WIN_H = 60
posX = 2 # position du héros
posY = 6
INIT_X = posX
INIT_Y = posY
NPC_MOVE_TIME = 0.2 # durée entre déplacement
posn1X = 25 # enemy 1 position
posn1Y = 6
NPC1_advance = 0 # initial position relative to path
NPC1_PATH_LENGTH = 15
right_n1 = True
left_n1 = not right_n1
posn2X = 78
posn2Y = 11
NPC2_advance = 24
NPC2_PATH_LENGTH = 24
right_n2 = False
left_n2 = not right_n2
posn3X = 5
posn3Y = 16
NPC3_advance = 0
NPC3_PATH_LENGTH = 60
right_n3 = True
left_n3 = not right_n3
posn4X = 164
posn4Y = 16
NPC4_advance = 87
NPC4_PATH_LENGTH = 87
right_n4 = False
left_n4 = not right_n4
posn5X = 88
posn5Y = 11
NPC5_advance = 0
NPC5_PATH_LENGTH = 40
right_n5 = True
left_n5 = not right_n5
posn6X = 43
posn6Y = 11
NPC6_advance = 30
NPC6_PATH_LENGTH = 30
right_n6 = False
left_n6 = not right_n6
posn7X = 140
posn7Y = 11
NPC7_advance = 0
NPC7_PATH_LENGTH = 24
right_n7 = True
left_n7 = not right_n7
posn8X = 8
posn8Y = 21
NPC8_advance = 0
NPC8_PATH_LENGTH = 100
right_n8 = True
left_n8 = not right_n8
posn9X = 6
posn9Y = 32
NPC9_advance = 0
NPC9_PATH_LENGTH = 152
right_n9 = True
left_n9 = not right_n9
POS_SHOOTX = 160 # position du shooter
POS_SHOOTY = 21
pos_arrowX = POS_SHOOTX-3 # position de la flèche
pos_arrowY = POS_SHOOTY+1
MAX_ADVANCE = 150 # deplacement max de la flèche
arrow_advance = 0 # déplacement de la flèche
POS_SHOOT2X = 160
POS_SHOOT2Y = 27
pos_arrow2X = POS_SHOOT2X-3
pos_arrow2Y = POS_SHOOT2Y+1
MAX_ADVANCE2 = 65
arrow_advance2 = 0
POS_SHOOT3X = 79
POS_SHOOT3Y = 27
pos_arrow3X = POS_SHOOT3X-3
pos_arrow3Y = POS_SHOOT3Y+1
MAX_ADVANCE3 = 54
arrow_advance3 = 0
POS_HEA_X = 115 # position d'un coeur
POS_HEA_Y = 3
n_lives = 3 # nombre de vies
REFRESH_TIME = 5 # refresh time du MainLoop()
PURPLE = 0 # couleurs
ORANGE = 1
HIGHLIGHT = 2
BLUE = 3
WHITE = 4
YELLOW = 5
RED = 6
ORANGE_ON_PURPLE = 1 # paires de couleurs
HIGHLIGHTED_PURPLE = 2
BLUE_ON_PURPLE = 3
WHITE_ON_PURPLE = 4
YELLOW_ON_PURPLE = 5
RED_ON_PURPLE = 6


def GameSetUp():
    """Prépare le jeu."""
    global screen # écran principal
    NUM_ROWS, NUM_COLS = screen.getmaxyx() # taille écran
    global X
    X = int(NUM_COLS/2 - WIDTH/2) # déterminé à partir de l'écran
    global main_win
    main_win = curses.newwin(MAIN_WIN_H, WIDTH, 0, X)
    curses.start_color() # initialisation des couleurs-paires
    curses.init_color(PURPLE, 112, 31, 132)
    curses.init_color(ORANGE, 1000, 500, 0)
    curses.init_color(RED, 1000, 200, 0)
    curses.init_color(HIGHLIGHT, 281, 16, 110)
    curses.init_color(YELLOW, 892, 892, 0)
    curses.init_color(BLUE, 0, 1000, 1000)
    curses.init_color(WHITE, 1000, 1000, 1000)
    curses.init_pair(ORANGE_ON_PURPLE, ORANGE, PURPLE)
    curses.init_pair(HIGHLIGHTED_PURPLE, ORANGE, HIGHLIGHT)
    curses.init_pair(BLUE_ON_PURPLE, BLUE, PURPLE)
    curses.init_pair(WHITE_ON_PURPLE, WHITE, PURPLE)
    curses.init_pair(YELLOW_ON_PURPLE,YELLOW, PURPLE)
    curses.init_pair(RED_ON_PURPLE,RED, PURPLE)
    curses.curs_set(0) # hide cursor
    curses.noecho() # no echo de l'input de l'utilisateur
    curses.cbreak()


def BD():
    """Affichage du BD."""
    global main_win
    y1 = 10
    y2 = 30
    y3 = 7
    y4 = 26
    x1 = 32
    x2 = 28
    x3 = 22
    t = 10
    main_win.clear() # un seul niveau
    main_win.refresh()
    time.sleep(1)
    maze.Afficher(main_win, COMIC1, x1, y1, ORANGE_ON_PURPLE)
    main_win.refresh()
    time.sleep(t)
    maze.Afficher(main_win, COMIC2, x2, y2, ORANGE_ON_PURPLE)
    main_win.refresh()
    time.sleep(t)
    main_win.clear()
    main_win.refresh()
    maze.Afficher(main_win, COMIC3, x3, y3, ORANGE_ON_PURPLE)
    main_win.refresh()
    time.sleep(t)
    maze.Afficher(main_win, COMIC4, x3, y4, ORANGE_ON_PURPLE)
    main_win.refresh()
    time.sleep(t)
    while True:
        key = main_win.getch()
        if key == ord("\n"):
            break
    main_win.clear()
    main_win.refresh()


def LevelChose(x_1, y_1, x_2, y_2, x_3, y_3):
    """Permet à l'utilisateur de choisir le niveau."""
    advance_l = 0
    key = main_win.getkey() # première fois n'importe quelle touche
    maze.Afficher(main_win, UI_LEVEL1, y_1, x_1, HIGHLIGHT) # highlight
    while True:
        key_l = main_win.getch()
        maze.Afficher(main_win, UI_LEVEL1, y_1, x_1, ORANGE_ON_PURPLE)
        maze.Afficher(main_win, UI_LEVEL2, y_2, x_2, ORANGE_ON_PURPLE)
        maze.Afficher(main_win, UI_LEVEL3, y_3, x_3, ORANGE_ON_PURPLE)
        if key_l == ord("d") and advance_l < 2:
            advance_l += 1 # déplacement du highlight
        if key_l == ord("a") and advance_l > 0:
            advance_l -= 1
        if advance_l == 0:
            maze.Afficher(main_win, UI_LEVEL1, y_1, x_1, HIGHLIGHT)
        elif advance_l == 1:
            maze.Afficher(main_win, UI_LEVEL2, y_2, x_2, HIGHLIGHT)
        elif advance_l == 2:
            maze.Afficher(main_win, UI_LEVEL3, y_3, x_3, HIGHLIGHT)
        if advance_l == 0 and key_l == ord("\n"): # selection
            BD()
            break


def LevelMenu():
    """Le menu des niveaux."""
    global main_win
    y_move = 6
    x_move = 60
    x, y = maze.Center(main_win, KDUZ_LINES, -20, MAIN_WIN_H, WIDTH)
    maze.Afficher(main_win, KDUZ_LINES, y, x, ORANGE_ON_PURPLE)
    x_1, y_1 = maze.Center(main_win, UI_LEVEL1, y_move, MAIN_WIN_H, WIDTH, decal_x=-x_move)
    x_2, y_2 = maze.Center(main_win, UI_LEVEL2, y_move, MAIN_WIN_H, WIDTH)
    x_3, y_3 = maze.Center(main_win, UI_LEVEL3, y_move, MAIN_WIN_H, WIDTH, decal_x=x_move)
    maze.Afficher(main_win, UI_LEVEL1, y_1, x_1, ORANGE_ON_PURPLE)
    maze.Afficher(main_win, UI_LEVEL2, y_2, x_2, ORANGE_ON_PURPLE) # affichage UI
    maze.Afficher(main_win, UI_LEVEL3, y_3, x_3, ORANGE_ON_PURPLE)
    LevelChose(x_1, y_1, x_2, y_2, x_3, y_3) # choix


def Help():
    """Le menu d'aide, qui explique comment jouer et l'objectif du jeu."""
    global help_menu
    help_menu = True
    main_win.clear()
    x, y = maze.Center(main_win, KDUZ_LINES, -20, MAIN_WIN_H, WIDTH)
    maze.Afficher(main_win, KDUZ_LINES, y, x, ORANGE_ON_PURPLE)
    x_3, y_3 = maze.Center(main_win, REGLES, 5, MAIN_WIN_H, WIDTH)
    maze.Afficher(main_win, REGLES, y_3, x_3, ORANGE_ON_PURPLE)
    while True:
        key2 = main_win.getch()
        if key2 == 27: # key = escape
            main_win.clear()
            main_win.refresh()
            break


def OptionChose(x_j, y_j, x_r, y_r, x_q, y_q):
    """Permet de chosir dans le menu. Choix entre quitter, regles et jouer."""
    global help_menu
    help_menu = False
    key = main_win.getkey() # une touche de clavier pour commencer
    maze.Afficher(main_win, M_JOUER_LINES, y_j, x_j, HIGHLIGHT)
    advance = 0
    first = True
    x, y = maze.Center(main_win, KDUZ_LINES, -20, MAIN_WIN_H, WIDTH)
    while True:
        if help_menu: # en revenant du menu help, réafficher
            maze.Afficher(main_win, KDUZ_LINES, y, x, ORANGE_ON_PURPLE)
            maze.Afficher(main_win, M_JOUER_LINES, y_j, x_j, ORANGE_ON_PURPLE)
            maze.Afficher(main_win, M_REGLES_LINES, y_r, x_r, ORANGE_ON_PURPLE)
            maze.Afficher(main_win, M_QUIT_LINES, y_q, x_q, ORANGE_ON_PURPLE)
            help_menu = False
        key = main_win.getch()
        maze.Afficher(main_win, M_JOUER_LINES, y_j, x_j, ORANGE_ON_PURPLE)
        maze.Afficher(main_win, M_REGLES_LINES, y_r, x_r, ORANGE_ON_PURPLE)
        maze.Afficher(main_win, M_QUIT_LINES, y_q, x_q, ORANGE_ON_PURPLE)
        if key == ord("s") and advance < 2:
            advance += 1
        elif key == ord("w") and advance > 0:
            advance -= 1
        if advance == 0:
            maze.Afficher(main_win, M_JOUER_LINES, y_j, x_j, HIGHLIGHT)
        if advance == 1:
            maze.Afficher(main_win, M_REGLES_LINES, y_r, x_r, HIGHLIGHT)
        if advance == 2:
            maze.Afficher(main_win, M_QUIT_LINES, y_q, x_q, HIGHLIGHT)
        if first and key == ord("w") or key == ord("s"):
            maze.Afficher(main_win, M_JOUER_LINES, y_j, x_j, ORANGE_ON_PURPLE)
            first = False
        if key == ord("\n") and advance == 0:
            main_win.clear()
            main_win.refresh() # jouer
            break
        if key == ord("\n") and advance == 1:
            Help() # obligé de ceci mettre ici, car nous ne voulons pas quitter la boucle des choix
        elif key == ord("\n") and advance == 2:
            return False


def Menu():
    """Menu."""
    global main_win
    # Affichage UI
    x, y = maze.Center(main_win, KDUZ_LINES, -20, MAIN_WIN_H, WIDTH)
    maze.Afficher(main_win, KDUZ_LINES, y, x, ORANGE_ON_PURPLE)
    x_j, y_j = maze.Center(main_win, M_JOUER_LINES, -5, MAIN_WIN_H, WIDTH)
    maze.Afficher(main_win, M_JOUER_LINES, y_j, x_j, ORANGE_ON_PURPLE)
    x_r, y_r = maze.Center(main_win, M_REGLES_LINES, 5, MAIN_WIN_H, WIDTH)
    maze.Afficher(main_win, M_REGLES_LINES, y_r, x_r, ORANGE_ON_PURPLE)
    x_q, y_q = maze.Center(main_win, M_QUIT_LINES, 15, MAIN_WIN_H, WIDTH)
    maze.Afficher(main_win, M_QUIT_LINES, y_q, x_q, ORANGE_ON_PURPLE)
    choice = OptionChose(x_j, y_j, x_r, y_r, x_q, y_q) # choix
    if choice == False:
        return False


def LevelSetUp():
    "Prépare le niveau."
    pos_hea_x = POS_HEA_X
    global top_win
    top_win = curses.newwin(TOP_WIN_H, WIDTH, 0, X)
    global bot_win
    bot_win = curses.newwin(BOT_WIN_H, WIDTH, TOP_WIN_H+1, X)
    bot_win.timeout(REFRESH_TIME)
    maze.Afficher(top_win, TOP_WIN_LINES, 0, 0, ORANGE_ON_PURPLE)
    maze.Afficher(top_win, SMALL_LOGO, 8, 3, ORANGE_ON_PURPLE)
    for i in range(n_lives):
        maze.Afficher(top_win, HEART_LINES, pos_hea_x, POS_HEA_Y, BLUE_ON_PURPLE)
        pos_hea_x += 17
    maze.Afficher(bot_win, LEVEL1_LINES, 0, 0, ORANGE_ON_PURPLE)
    maze.Afficher(bot_win, SHOOTER, POS_SHOOTX, POS_SHOOTY, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, SHOOTER, POS_SHOOT2X, POS_SHOOT2Y, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, SHOOTER, POS_SHOOT3X, POS_SHOOT3Y, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, HERO_LINES, posX, posY, ORANGE_ON_PURPLE)
    bot_win.refresh()
    top_win.refresh()


def FloconPos():
    """
    Détermine la position des flocons. Les positions ont été choisis
    manuellement.
    """
    global star_pos, n_stars
    star_pos = []
    y2 = 7
    step = 3
    n_stars = 0
    for x in range(10, 18, step): # boucle pour trouver les positions des flocons
        star_pos += maze.AllPositions(FLOCON, x, y2)
        n_stars += 1
    for x in range(26, 44, step):
        star_pos += maze.AllPositions(FLOCON, x, y2)
        n_stars += 1
    for x in range(52, 53):
        star_pos += maze.AllPositions(FLOCON, x, y2)
        n_stars += 1
    y1 = 6
    for x in range(60, 61, step):
        star_pos += maze.AllPositions(FLOCON, x, y1)
        n_stars += 1
    for x in range(125, 148, step):
        star_pos += maze.AllPositions(FLOCON, x, y1)
        n_stars += 1
    for x in range(157, 167, step):
        star_pos += maze.AllPositions(FLOCON, x, y1)
        n_stars += 1
    y0 = 5
    for x in range(65, 90, step):
        star_pos += maze.AllPositions(FLOCON, x, y0)
        n_stars += 1
    y3 = 12
    for x in range(13, 47, step):
        star_pos += maze.AllPositions(FLOCON, x, y3)
        n_stars += 1
    for x in range(55, 80, step):
        star_pos += maze.AllPositions(FLOCON, x, y3)
        n_stars += 1
    for x in range(89, 133, step):
        star_pos += maze.AllPositions(FLOCON, x, y3)
        n_stars += 1
    for x in range(141, 156, step):
        star_pos += maze.AllPositions(FLOCON, x, y3)
        n_stars += 1
    y4 = 17
    for x in range(6, 70, step):
        star_pos += maze.AllPositions(FLOCON, x, y4)
        n_stars += 1
    for x in range(78, 156, step):
        star_pos += maze.AllPositions(FLOCON, x, y4)
        n_stars += 1
    y5 = 22
    for x in range(4, 123, step):
        star_pos += maze.AllPositions(FLOCON, x, y5)
        n_stars += 1
    y6 = 28
    for x in range(9, 13, step):
        star_pos += maze.AllPositions(FLOCON, x, y6)
        n_stars += 1
    for x in range(23, 33, step):
        star_pos += maze.AllPositions(FLOCON, x, y6)
        n_stars += 1
    for x in range(95, 130, step):
        star_pos += maze.AllPositions(FLOCON, x, y6)
        n_stars += 1
    y7 = 33
    for x in range(8, 160, step):
        star_pos += maze.AllPositions(FLOCON, x, y7)
        n_stars += 1


def FloconsAffichage(star_pos):
    """Affichage des flocons."""
    for i in star_pos:
        maze.Afficher(bot_win, FLOCON, i[1], i[0], WHITE_ON_PURPLE)


def FloconCollection(hero_pos):
    """Compte le nombre de flocons collectés et enlève ceux déja pris."""
    global stars
    if maze.IsSuperposed(hero_pos, star_pos): # si pris, collectionné
        for i in star_pos:
            if i in hero_pos:
                maze.Effacer(bot_win, FLOCON, i[1], i[0])
                star_pos.remove(i) # important, pour que le flocons pris ne soient pas affichés
                stars += 1


def NPCNewPos(NPC1_advance, posn1X, right_n1, left_n1, path_length):
    """Detrmine la prochaine position de l'ennemi."""
    if NPC1_advance == path_length:
        left_n1 = True
        right_n1 = False # max --> gauche
    if NPC1_advance == 0:
        right_n1 = True
        left_n1 = False # min --> droite
    if left_n1:
        right_n1 = False
        posn1X -= 1
        NPC1_advance -= 1 # reculé de 1
    if right_n1:
        left_n1 = False
        posn1X += 1
        NPC1_advance += 1
    return posn1X, NPC1_advance, right_n1, left_n1


def NPC(t_p, t_ecoule, posnX, posnY, NPC_advance, right_n, left_n, NPC_PATH_LENGTH):
    """
    Change la position du bot si un certain temps s'est écoulé. Efface la
    position précédente.
    """
    if t_ecoule >= t_p: # est-il temps de se déplacer ?
        maze.Effacer(bot_win, NPC_LINES, posnX, posnY)
        posnX, NPC_advance, right_n, left_n = NPCNewPos(NPC_advance, posnX, right_n, left_n, NPC_PATH_LENGTH)
        t_p += NPC_MOVE_TIME # prochain mouvement
    return t_p, posnX, NPC_advance, right_n, left_n


def DeathAnimation():
    """
    Death animation.
    Changement des couleurs des bots et flèches. Time sleep.
    Effet de "melt".
    """
    maze.Afficher(bot_win, ARROW, pos_arrowX, pos_arrowY, RED_ON_PURPLE)
    maze.Afficher(bot_win, ARROW, pos_arrow2X, pos_arrow2Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, ARROW, pos_arrow3X, pos_arrow3Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn1X, posn1Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn2X, posn2Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn3X, posn3Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn4X, posn4Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn5X, posn5Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn6X, posn6Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn7X, posn7Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn8X, posn8Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn9X, posn9Y, RED_ON_PURPLE)
    bot_win.refresh()
    top_win.refresh()
    curses.napms(1000)
    maze.Effacer(bot_win, HERO_LINES, posX, posY)
    maze.Afficher(bot_win, HALF_DEAD, posX, posY, BLUE_ON_PURPLE)
    maze.Afficher(bot_win, ARROW, pos_arrowX, pos_arrowY, RED_ON_PURPLE)
    maze.Afficher(bot_win, ARROW, pos_arrow2X, pos_arrow2Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, ARROW, pos_arrow3X, pos_arrow3Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn1X, posn1Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn2X, posn2Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn3X, posn3Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn4X, posn4Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn5X, posn5Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn6X, posn6Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn7X, posn7Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn8X, posn8Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn9X, posn9Y, RED_ON_PURPLE)
    bot_win.refresh()
    top_win.refresh()
    curses.napms(1000)
    maze.Effacer(bot_win, HALF_DEAD, posX, posY)
    maze.Afficher(bot_win, DEAD, posX, posY, BLUE_ON_PURPLE)
    maze.Afficher(bot_win, ARROW, pos_arrowX, pos_arrowY, RED_ON_PURPLE)
    maze.Afficher(bot_win, ARROW, pos_arrow2X, pos_arrow2Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, ARROW, pos_arrow3X, pos_arrow3Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn1X, posn1Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn2X, posn2Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn3X, posn3Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn4X, posn4Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn5X, posn5Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn6X, posn6Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn7X, posn7Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn8X, posn8Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn9X, posn9Y, RED_ON_PURPLE)
    bot_win.refresh()
    top_win.refresh()
    curses.napms(1000)
    maze.Effacer(bot_win, DEAD, posX, posY)
    maze.Afficher(bot_win, ARROW, pos_arrowX, pos_arrowY, RED_ON_PURPLE)
    maze.Afficher(bot_win, ARROW, pos_arrow2X, pos_arrow2Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, ARROW, pos_arrow3X, pos_arrow3Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn1X, posn1Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn2X, posn2Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn3X, posn3Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn4X, posn4Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn5X, posn5Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn6X, posn6Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn7X, posn7Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn8X, posn8Y, RED_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn9X, posn9Y, RED_ON_PURPLE)
    bot_win.refresh()
    top_win.refresh()
    curses.napms(1000)


def Shooter(t_s, t_ecoule, pos_arrowX, pos_arrowY, arrow_advance, MAX_ADVANCE, init_pos):
    if t_ecoule >= t_s: # est il temps ?
        maze.Effacer(bot_win, ARROW, pos_arrowX, pos_arrowY)
        bot_win.refresh()
        pos_arrowX -= 1 # avance
        arrow_advance += 1
        if arrow_advance == MAX_ADVANCE:
            maze.Effacer(bot_win, ARROW, pos_arrowX, pos_arrowY) # despwan
            bot_win.refresh()
            pos_arrowX = init_pos
            arrow_advance = 0
        t_s += 0.05
    return t_s, pos_arrowX, arrow_advance


def Affichage():
    """
    Affichge du héros, bots, flèches.
    Cela s'affiche à chaque Update.
    """
    FloconsAffichage(star_pos)
    maze.Afficher(bot_win, HERO_LINES, posX, posY, BLUE_ON_PURPLE)
    maze.Afficher(bot_win, ARROW, pos_arrowX, pos_arrowY, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, ARROW, pos_arrow2X, pos_arrow2Y, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, ARROW, pos_arrow3X, pos_arrow3Y, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn1X, posn1Y, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn2X, posn2Y, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn3X, posn3Y, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn4X, posn4Y, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn5X, posn5Y, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn6X, posn6Y, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn7X, posn7Y, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn8X, posn8Y, YELLOW_ON_PURPLE)
    maze.Afficher(bot_win, NPC_LINES, posn9X, posn9Y, YELLOW_ON_PURPLE)
    bot_win.refresh()
    top_win.refresh()


def GameOver(result, color):
    """Affichage du gameover et attente de "esc" pour arrêter le jeu."""
    time.sleep(2)
    bot_win.clear()
    bot_win.refresh()
    x_logo, y_logo = maze.Center(bot_win, result, -6, BOT_WIN_H, WIDTH)
    maze.Afficher(bot_win, result, y_logo, x_logo, color)
    while True:
        key3 = bot_win.getch()
        if key3 == 27: # attend un escape
            break


def MainLoop():
    """Le jeu lui même. Refresh 5ms."""
    global posX, posY, posn1X, posn1Y, NPC1_advance, right_n1, left_n1
    global posn2X, posn2Y, NPC2_advance, right_n2, left_n2
    global posn3X, posn3Y, NPC3_advance, right_n3, left_n3 # variables qui vont être modifiées
    global posn4X, posn4Y, NPC4_advance, right_n4, left_n4
    global posn5X, posn5Y, NPC5_advance, right_n5, left_n5
    global posn6X, posn6Y, NPC6_advance, right_n6, left_n6
    global posn7X, posn7Y, NPC7_advance, right_n7, left_n7
    global posn8X, NPC8_advance, right_n8, left_n8
    global posn9X, posn9Y, NPC9_advance, right_n9, left_n9
    global pos_arrowX, arrow_advance
    global pos_arrow2X, arrow_advance2
    global pos_arrow3X, arrow_advance3
    global stars
    lives_left = n_lives
    t_p1 = 0
    t_p2 = 0.1
    t_p3 = 0.25
    t_p4 = 0.34
    t_p5 = 0.27
    t_p6 = 0.41
    t_p7 = 0.33
    t_p8 = 0.63 # temps different pour chaque bot, déplacement en décalé
    t_p9 = 0.2
    t_s = 0
    t_s2 = 0.5
    t_s3 = 0.7
    hx = POS_HEA_X
    start_time = time.time()
    y1 = 7
    stars = 0
    FloconPos()
    while True:
        oldX, oldY = posX, posY
        touche = bot_win.getch()
        t_ecoule = time.time() - start_time # temps
        # Calcule de la (nouvelle ou pas) position de chaque bot
        t_p1, posn1X, NPC1_advance, right_n1, left_n1 = NPC(t_p1, t_ecoule, posn1X, posn1Y, NPC1_advance, right_n1, left_n1, NPC1_PATH_LENGTH)
        t_p2, posn2X, NPC2_advance, right_n2, left_n2 = NPC(t_p2, t_ecoule, posn2X, posn2Y, NPC2_advance, right_n2, left_n2, NPC2_PATH_LENGTH)
        t_p3, posn3X, NPC3_advance, right_n3, left_n3 = NPC(t_p3, t_ecoule, posn3X, posn3Y, NPC3_advance, right_n3, left_n3, NPC3_PATH_LENGTH)
        t_p4, posn4X, NPC4_advance, right_n4, left_n4 = NPC(t_p4, t_ecoule, posn4X, posn4Y, NPC4_advance, right_n4, left_n4, NPC4_PATH_LENGTH)
        t_p5, posn5X, NPC5_advance, right_n5, left_n5 = NPC(t_p5, t_ecoule, posn5X, posn5Y, NPC5_advance, right_n5, left_n5, NPC5_PATH_LENGTH)
        t_p6, posn6X, NPC6_advance, right_n6, left_n6 = NPC(t_p6, t_ecoule, posn6X, posn6Y, NPC6_advance, right_n6, left_n6, NPC6_PATH_LENGTH)
        t_p7, posn7X, NPC7_advance, right_n7, left_n7 = NPC(t_p7, t_ecoule, posn7X, posn7Y, NPC7_advance, right_n7, left_n7, NPC7_PATH_LENGTH)
        t_p8, posn8X, NPC8_advance, right_n8, left_n8 = NPC(t_p8, t_ecoule, posn8X, posn8Y, NPC8_advance, right_n8, left_n8, NPC8_PATH_LENGTH)
        t_p9, posn9X, NPC9_advance, right_n9, left_n9 = NPC(t_p9, t_ecoule, posn9X, posn9Y, NPC9_advance, right_n9, left_n9, NPC9_PATH_LENGTH)
        t_s, pos_arrowX, arrow_advance = Shooter(t_s, t_ecoule, pos_arrowX, pos_arrowY,arrow_advance, MAX_ADVANCE, POS_SHOOTX-3)
        # Calcule de la (nouvelle ou pas) position de chaque flèche
        t_s2, pos_arrow2X, arrow_advance2 = Shooter(t_s2, t_ecoule, pos_arrow2X, pos_arrow2Y, arrow_advance2, MAX_ADVANCE2, POS_SHOOT2X-3)
        t_s3, pos_arrow3X, arrow_advance3 = Shooter(t_s3, t_ecoule, pos_arrow3X, pos_arrow3Y, arrow_advance3, MAX_ADVANCE3, POS_SHOOT3X-3)
        # position fleches + bots
        danger_pos = maze.AllPositions(NPC_LINES, posn1X, posn1Y) + maze.AllPositions(NPC_LINES, posn2X, posn2Y) + maze.AllPositions(NPC_LINES, posn3X, posn3Y) + maze.AllPositions(NPC_LINES, posn4X, posn4Y) + maze.AllPositions(NPC_LINES, posn5X, posn5Y) + maze.AllPositions(NPC_LINES, posn6X, posn6Y) + maze.AllPositions(NPC_LINES, posn7X, posn7Y) + maze.AllPositions(NPC_LINES, posn8X, posn8Y) + maze.AllPositions(ARROW, pos_arrowX, pos_arrowY) + maze.AllPositions(SHOOTER, POS_SHOOTX, POS_SHOOTY) + maze.AllPositions(ARROW, pos_arrow2X, pos_arrow2Y) + maze.AllPositions(SHOOTER, POS_SHOOT2X, POS_SHOOT2Y) + maze.AllPositions(ARROW, pos_arrow3X, pos_arrow3Y) + maze.AllPositions(SHOOTER, POS_SHOOT3X, POS_SHOOT3Y)
        if maze.IsSuperposed(maze.AllPositions(HERO_LINES, posX, posY), danger_pos): # touche ?
            DeathAnimation()
            lives_left -= 1
            maze.Effacer(top_win, HEART_LINES, hx, POS_HEA_Y)
            top_win.refresh()
            hx += 17 # Changement du coeur
            posX, posY = INIT_X, INIT_Y
        if lives_left == 0:
            GameOver(GAME_OVER, RED_ON_PURPLE) # perdu !
            break
        if stars == n_stars:
            GameOver(VICTORY, YELLOW_ON_PURPLE) # gagné !
            break
        posX, posY = maze.NewPos(screen, posX, posY, HERO_LINES, 0, 0, LEVEL1_LINES, touche) # input, postion héros
        hero_pos = maze.AllPositions(HERO_LINES, posX, posY)
        FloconCollection(hero_pos) # enlève les flocons pris
        if (oldX, oldY) != (posX, posY): # seulement effacer si déplacement
            maze.Effacer(bot_win, HERO_LINES, oldX, oldY)
        Affichage() # Tout afficher
        if touche == 27: # escape --> arrêter
            bot_win.clear()
            bot_win.refresh()
            time.sleep(2)
            break


if __name__ == "__main__":
    try:
        screen = curses.initscr()
        GameSetUp()
        ch = Menu()
        if ch == None: # pas False, donc pas quitter --> aucun return
            LevelMenu()
            LevelSetUp()
            MainLoop()
        curses.endwin()
    except:
        curses.wrapper(MainLoop)
