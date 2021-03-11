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


printGrille(grille)

for move in range(1, 61):
    print("Tour " + str(move))
    if move % 2 == 1:
        while True:
            column_j1 = int(input("Joueur 1, entrez la colonne : "))
            row_j1 = int(input("Joueur 1, entrez une ligne : "))

            if 1 <= column_j1 <= 8 and 1 <= row_j1 <= 8:
                if grille[row_j1][column_j1] == ".":
                    grille[row_j1][column_j1] = "o"
                    break
                else:
                    print("Ces champ sont deja pris")
            else:
                print("ce ne sont pas des champs valides")

        printGrille(grille)

    elif move % 2 == 0:
        while True:
            column_j2 = int(input("Joueur 2, entrez la colonne : "))
            row_j2 = int(input("Joueur 2, entrez une ligne : "))

            if 1 <= column_j2 <= 8 and 1 <= row_j2 <= 8:
                if grille[row_j2][column_j2] == ".":
                    grille[row_j2][column_j2] = "x"
                    break
                else:
                    print("Ces champ sont deja pris")
            else:
                print("Cs ne sont pas des champs valides")

printGrille(grille)


