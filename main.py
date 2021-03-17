import math
import os
import functions
# Grille d'Othello

grille = []
for row in range(0, 10):
    grille.append([])
    if row == 0:
        grille[row].append(" ")
        for column in range(1, 10):
            if column == 9:
                grille[row].append("_")
            else:
                grille[row].append(column)
    elif row == 9:
        for column in range(1, 10):
            grille[row].append("_")
    else:
        grille[row].append(row)
        for column in range(1, 10):
            if column == 9:
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

# formatage affichage de la grille
# ///////////////// DEBUT PARTIE /////////////////////
functions.cls()
functions.printGrille(grille)

# Les coups des uilisatuers se lancent
for move in range(1, 61):
    print("Tour " + str(move))
    if move % 2 == 1:
        while True:
            column_j1 = int(input("Joueur 1, entrez la colonne : "))
            row_j1 = int(input("Joueur 1, entrez une ligne : "))

            if 1 <= column_j1 <= 8 and 1 <= row_j1 <= 8:
                if functions.check_autour(grille, row_j1, column_j1) and grille[row_j1][column_j1] == ".":
                    grille[row_j1][column_j1] = "o"
                    break
                else:
                    print("Placement non autorisé... Regardez les regles du jeu, merci.")
            else:
                print("Placement non autorisé... Regardez les regles du jeu, merci.")

        functions.return_o_horizontal(grille, row_j1, column_j1)
        functions.return_o_vertical(grille, row_j1, column_j1)
        functions.return_o_diagonal(grille, row_j1, column_j1)

    if move % 2 == 0:
        while True:
            column_j2 = int(input("Joueur 2, entrez la colonne : "))
            row_j2 = int(input("Joueur 2, entrez une ligne : "))

            if 1 <= column_j2 <= 8 and 1 <= row_j2 <= 8:
                if functions.check_autour(grille, row_j2, column_j2) and grille[row_j2][column_j2] == ".":
                    grille[row_j2][column_j2] = "x"
                    break
                else:
                    print("Placement non autorisé... Regardez les regles du jeu, merci.")
            else:
                print("Placement non autorisé... Regardez les regles du jeu, merci.")
        
        functions.return_x_horizontal(grille, row_j2, column_j2)
        functions.return_x_vertical(grille, row_j2, column_j2)


    functions.cls()
    functions.printGrille(grille)

# ceci est un test un vrai test

