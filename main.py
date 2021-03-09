import math
# Grille d'Othello

grille = []
for row in range(0,9):
    grille.append([])
    if row == 0:
        grille[row].append(" ")
        for element in range(1,9):                
            grille[row].append(element)

    else:
        grille[row].append(row)
        for element in range(1,9):
            grille[row].append(".")

#etablir une position de depart
milieu_ligne = int(math.ceil(len(grille)) / 2)
milieu_colonne = int(math.ceil(len(grille[0])) /2)

grille[milieu_ligne][milieu_colonne] = "x" 
grille[milieu_ligne + 1][milieu_colonne + 1] = "x" 
grille[milieu_ligne][milieu_colonne + 1] = "o" 
grille[milieu_ligne + 1][milieu_colonne] = "o" 

#formatage affichage de la grille
def printGrille(grille_par):
    for element in grille_par:
        for truc in element:
            print(truc, end=" ")
        print()

printGrille(grille)

for move in range(1, 61):
    print("Tour " + str(move))
    if move % 2 == 1:
        column_j1 = int(input("Joueur 1, entrez la colonne : "))
        row_j1 = int(input("Joueur 1, entrez une ligne : "))

        if 1 > column_j1 > 8 or 1 > row_j1 > 8:
            print("ce ne sont pas des champs valides")
        elif grille[row_j1][column_j1] == ".":
            grille[row_j1][column_j1] = "o"
            printGrille(grille)
        elif grille[row_j1][column_j1] == "o" or grille[row_j1][column_j1] == "x":
            print("ce champ est deja pris")

    elif move % 2 == 0:
        column_j2 = int(input("Joueur 2, entrez entrez la colonne : "))
        row_j2 = int(input("Joueur 2, entrez une ligne : "))

        if 1 > column_j2 > 8 or 1 > row_j2 > 8:
            print("ce ne sont pas des champs valides")
        elif grille[row_j2][column_j2] == ".":
            grille[row_j2][column_j2] = "x"
            printGrille(grille)
        elif grille[row_j2][column_j2] == "o" or grille[row_j2][column_j2] == "x":
            print("ce champ est deja pris")


print("hello matis")