import math
import os
import functions
from damier import Damier
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

while True:
    try:
        taille = int(input(" Quelle taille de plateau voulez-vous ? Entrez une valeur paire, d'au moins 4 : "))
        if taille >= 4 and taille % 2 == 0:
            break
        else:
            print("Votre valeur n'est pas valide, entre en une autre.")
    except:
        print("Veuillez entrer un nombre entier...")


# Création du widget principal ("maître") :
fen1 = Tk()
fen1.iconphoto(True, PhotoImage(file='icon.png'))
# taille = IntVar()
# taille_input = ttk.Entry(fen1, textvariable=taille)

# Création des widgets "esclaves" :
can1 = Canvas(fen1, bg='light steel blue', height=taille*37, width=taille*37)
can1.pack(side=LEFT)


# Creation du damier
d = Damier(can1)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)

#can1.bind("<Button-1>", d.pointeur)  # on rajoute un evenement "pointeur" quand on clique gauche
bou2 = Button(fen1, text='Jouer', command= lambda : d.creation_grille(taille))
bou2.pack(side=TOP)
bou3 = Button(fen1, text='Effacer', command=d.clear)
bou3.pack()

can1.bind('<Button-1>', d.posePion)

fen1.mainloop()  # démarrage du réceptionnaire d'événement
fen1.destroy()  # destruction (fermeture) de la fenêtre


grille = []
for row in range(0, taille + 2):
    grille.append([])
    if row == 0:
        grille[row].append(" ")
        
        for column in range(1, taille + 2):
            if column == taille + 1:
                grille[row].append("_")
            else:
                grille[row].append(column)
    elif row == taille + 1:
        for column in range(0, taille + 2):
            grille[row].append("_")
    else:
        grille[row].append(row)
        for column in range(1, taille + 2):
            if column == taille + 1:
                grille[row].append("_")
            else:
                grille[row].append(".")

# etablir une position de depart
milieu_ligne = int(math.floor(len(grille) - 1) / 2)
milieu_colonne = int(math.floor(len(grille[0]) - 1) / 2)

grille[milieu_ligne][milieu_colonne] = "x"
grille[milieu_ligne + 1][milieu_colonne + 1] = "x"
grille[milieu_ligne][milieu_colonne + 1] = "o"
grille[milieu_ligne + 1][milieu_colonne] = "o"

# ///////////////// DEBUT PARTIE /////////////////////
#functions.cls()
functions.printGrille(grille)

# Les coups des uilisatuers se lancent
for move in range(1, 61):
    print("Tour " + str(move))
    if move % 2 == 1: #player 1 move
        player = "Joueur 1"
        row, column = functions.user_move(grille, player)
        functions.flip_horizontal(grille, player, row, column)
        functions.flip_vertical(grille, player, row, column)
        functions.flip_diagonal(grille, player, row, column)

    if move % 2 == 0: #player 2 move
        player = "Joueur 2"
        row, column = functions.user_move(grille, player)
        functions.flip_horizontal(grille, player, row, column)
        functions.flip_vertical(grille, player, row, column)
        functions.flip_diagonal(grille, player, row, column)

    #functions.cls()
    functions.printGrille(grille)

functions.is_winner(grille)
