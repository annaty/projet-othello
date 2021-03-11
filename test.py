import math
# Grille d'Othello

grille = []
for row in range(0, 9):
    grille.append([])
    if row == 0:
        grille[row].append(" ")
        for column in range(1, 9):
            grille[row].append(column)

    else:
        grille[row].append(row)
        for column in range(1, 9):
            grille[row].append(".")

# etablir une position de depart
milieu_ligne = int(math.ceil(len(grille)) / 2)
milieu_colonne = int(math.ceil(len(grille[0])) / 2)

grille[milieu_ligne][milieu_colonne] = "x"
grille[milieu_ligne + 1][milieu_colonne + 1] = "x"
grille[milieu_ligne][milieu_colonne + 1] = "o"
grille[milieu_ligne + 1][milieu_colonne] = "o"

# formatage affichage de la grille


def printGrille(grille_par):
    for element in grille_par:
        for truc in element:
            print(truc, end=" ")
        print()

for row in grille:
    for champ in row:
        # if pion == "x" and row[row.index(pion) + 1] == "o" and row[row.index(pion) - 1] == "o":
        #     row[row.index(pion)] == "o"
        my_index = row.index(champ) # my column that i want to change things in !!!
        if my_index == 3:
            champ = "0"

printGrille(grille)

