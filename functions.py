#functions
import os

# Fonction qui affiche la grille
def printGrille(grille_par):
    for element in grille_par:
        for truc in element:
            print(truc, end=" ")
        print()

# Fonction clear le terminal
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fonction qui vérifié ce que l'on a autour du pion qu'on joue
def check_autour(grille, row, column):
    if (grille[row - 1][column] != "x" and grille[row + 1][column] != "x" and grille[row][column - 1] != "x" 
            and grille[row][column + 1] != "x" and grille[row + 1][column - 1] != "x" and grille[row + 1][column + 1] != "x" 
            and grille[row - 1][column - 1] != "x" and grille[row - 1][column + 1] != "x" and grille[row - 1][column] != "o" 
            and grille[row + 1][column] != "o" and grille[row][column - 1] != "o" and grille[row][column + 1] != "o" 
            and grille[row + 1][column - 1] != "o" and grille[row + 1][column + 1] != "o" and grille[row - 1][column - 1] != "o" and grille[row - 1][column + 1] != "o"):
        return False
    else:
        return True

# Fonction qui retourne les pions "o" à l'horizontale
def return_o_horizontal(grille, row_j1, column_j1):
    for element in range(len(grille[row_j1])):
        if grille[row_j1][element] == "o" and element != column_j1:
            if element < column_j1:
                for index_transform in range(element, column_j1):
                    grille[row_j1][index_transform] = "o"
            else:
                for index_transform in range(column_j1, element):
                    grille[row_j1][index_transform] = "o"
            break

# Fonction qui retourne les pions "x" à l'horizontale
def return_x_horizontal(grille, row_j2, column_j2):
    for element in range(len(grille[row_j2])):
        if grille[row_j2][element] == "x" and element != column_j2:
            if element < column_j2:
                for index_transform in range(element, column_j2):
                    grille[row_j2][index_transform] = "x"
            else:
                for index_transform in range(column_j2, element):
                    grille[row_j2][index_transform] = "x"
            break

# Fonction qui retourne les pions "o" à la verticale
def return_o_vertical(grille, row_j1, column_j1):
    for row_index in range(len(grille)):
        if grille[row_index][column_j1] == "o" and row_index != row_j1:
                if row_index < row_j1:
                    for index_transform in range(row_index, row_j1 + 1):
                        grille[index_transform][column_j1] = "o"
                else:
                    for index_transform in range(row_j1, row_index + 1):
                        grille[index_transform][column_j1] = "o"
                break

# Fonction qui retourne les pions "x" à la verticale
def return_x_vertical(grille, row_j2, column_j2):
    for row_index in range(len(grille)):
        if grille[row_index][column_j2] == "x" and row_index != row_j2:
                if row_index < row_j2:
                    for index_transform in range(row_index, row_j2 + 1):
                        grille[index_transform][column_j2] = "x"
                else:
                    for index_transform in range(row_j2, row_index + 1):
                        grille[index_transform][column_j2] = "x"
                break

#def return_x_diagonal(grille, row_j2, column_j2):

# Fonction qui retourne les pions "o" en diagonale
def return_o_diagonal(grille, row_j1, column_j1):
    for i in range(1, 2):
        if grille[row_j1 + i][column_j1 + i] == "o": # SE
            for index_transform in range(1, i):
                grille[row_j1 + i][column_j1 + i] = "o"
        elif grille[row_j1 - i][column_j1 - i] == "o": # NO
            for index_transform in range(1, i):
                grille[row_j1 - i][column_j1 - i] = "o"
        elif grille[row_j1 + i][column_j1 - i] == "o": # SO
            for index_transform in range(1, i):
                grille[row_j1 + i][column_j1 - i] = "o"
        elif grille[row_j1 - i][column_j1 + i] == "o": # NE
            for index_transform in range(1, i):
                grille[row_j1 - i][column_j1 + i] = "o"