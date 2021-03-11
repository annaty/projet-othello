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

def check_autour(row, column):
    if row == 1 and column == 1:
        if grille[row][column + 1] == "." and grille[row + 1][column] == "." and grille[row + 1][column + 1] == ".":
            return False
    elif row == 1 and column == (len(grille[1]) - 1):
        if grille[row][column - 1] == "." and grille[row + 1][column] == "." and grille[row + 1][column - 1] == ".":
            return False
    elif row == (len(grille) - 1) and column == 1:
        if grille[row][column + 1] == "." and grille[row - 1][column] == "." and grille[row - 1][column + 1] == ".":
            return False
    elif row == (len(grille) - 1) and column == (len(grille[1]) - 1):
        if grille[row][column - 1] == "." and grille[row - 1][column] == "." and grille[row - 1][column - 1] == ".":
            return False   
    elif row == 1:
        if grille[row][column - 1] == "." and grille[row][column + 1] == "." and grille[row+1][column] == "." and grille[row + 1][column - 1] == "." and grille[row + 1][column + 1] == ".":
            return False 
    elif column == 1:
        if grille[row][column + 1] == "." and grille[row - 1][column] == "." and grille[row + 1][column] == "." and grille[row - 1][column + 1] == "." and grille[row + 1][column + 1] == ".":
            return False 
    elif row == (len(grille) - 1):
        if grille[row][column - 1] == "." and grille[row][column + 1] == "." and grille[row - 1][column] == "." and grille[row - 1][column + 1] == "." and grille[row - 1][column - 1] == ".":
            return False
    elif column == (len(grille[1]) - 1):
        if grille[row][column - 1] == "." and grille[row + 1][column] == "." and grille[row - 1][column] == "." and grille[row + 1][column - 1] == "." and grille[row - 1][column - 1] == ".":
            return False
    elif grille[row - 1][column] == "." and grille[row + 1][column] == "." and grille[row][column - 1] == "." and grille[row][column + 1] == "." and grille[row + 1][column - 1] == "." and grille[row + 1][column + 1] == "." and grille[row - 1][column - 1] == "." and grille[row - 1][column + 1] == ".":
        return False
    else: 
        return True

printGrille(grille)

for move in range(1, 61):
    print("Tour " + str(move))
    if move % 2 == 1:
        while True:
            column_j1 = int(input("Joueur 1, entrez la colonne : "))
            row_j1 = int(input("Joueur 1, entrez une ligne : "))

            if 1 <= column_j1 <= 8 and 1 <= row_j1 <= 8:
                if  check_autour(row_j1, column_j1) and grille[row_j1][column_j1] == ".":
                    grille[row_j1][column_j1] = "o"
                    break
                else:
                    print("Ces champ ne sont pas valides.")
            else:
                print("Ce ne sont pas des champs valides")

        #printGrille(grille)

    elif move % 2 == 0:
        while True:
            column_j2 = int(input("Joueur 2, entrez la colonne : "))
            row_j2 = int(input("Joueur 2, entrez une ligne : "))

            if 1 <= column_j2 <= 8 and 1 <= row_j2 <= 8:
                if check_autour(row_j2, column_j2) and grille[row_j2][column_j2] == ".":
                    grille[row_j2][column_j2] = "x"
                    break
                else:
                    print("Ces champ ne sont pas valides.")
            else:
                print("Ces champ ne sont pas valides.")

        #printGrille(grille)




