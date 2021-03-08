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

for move in range(1, 61):
    print("Move number" + str(move))
    if move % 2 == 0
        column_j1 = int(input("Joueur 1, entrez une ligne : "))
        ligne_j1 = 
    else:
    
#formatage affichage de la grille
def printGrille():
    for element in grille:
        for truc in element:
            print(truc, end=" ")
        print()

printGrille()

