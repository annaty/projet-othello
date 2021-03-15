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


def return_x_horizontal():
    # ça retourne x à l'horizontal
    for row_index in range(len(grille)):
        start = -1
        end = -1
        for column_index in range(len(grille[1])):
            if grille[row_index][column_index] == "x":
                if start == -1:
                    start = column_index
                else :
                    end = column_index
        for index_transform in range(start, end):
            grille[row_index][index_transform] = "x"

def return_o_horizontal():
    # ça retourne o à l'horizontal
    for row_index in range(len(grille)):
        start = -1
        end = -1
        for column_index in range(len(grille[1])):
            if grille[row_index][column_index] == "o":
                if start == -1:
                    start = column_index
                else :
                    end = column_index
        for index_transform in range(start, end):
            grille[row_index][index_transform] = "o"

# def return_x_vertical():
#     # ça retourne x à la vertical
#     for row_index in range(len(grille)):
#         for column_index in range(len(grille[1])):
#             if grille[row_index][column_index] == "x" and row_index != row_j2 and column_index == column_j2:
#                 row_ref = row_index
#                 break
#     if row_ref < row_j2:
#         for index_transform in range(row_ref, row_j2 + 1):
#             grille[index_transform][column_j1] = "x"
#     else:
#         for index_transform in range(row_j2, row_ref + 1):
#             grille[index_transform][column_j1] = "x"

# def return_o_vertical():
#     # ça retourne o à la vertical
#     for row_index in range(len(grille)):
#         for column_index in range(len(grille[1])):
#             if grille[row_index][column_index] == "o" and row_index != row_j1 and column_index == column_j1:
#                 row_ref = row_index
#                 break

#     if row_ref < row_j1:
#         for index_transform in range(row_ref, row_j1 + 1):
#             grille[index_transform][column_j1] = "o"
#     else:
#         for index_transform in range(row_j1, row_ref + 1):
#             grille[index_transform][column_j1] = "o"


printGrille(grille)



# Les coups des uilisatuers se lancent
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
        
        return_o_horizontal()


        # printGrille(grille)

    if move % 2 == 0:
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
        
        return_x_horizontal()


    
    printGrille(grille)




