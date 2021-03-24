def clear_helpers(move_list, counter):
    move_list.clear()
    counter = 0

def empty_cell_in_list(grille, row, column):


def flip(grille, player, row, column):
    if player == "Joueur 1":
        player_piece = "o"
        enemy_piece = "x"
    elif player == "Joueur 2":
        player_piece = "x"
        enemy_piece = "o"

    check_list = []
    i = 0

    while reached_limit(check_list, len(grille[1])) == False:
        i += 1
        east_cell_content = grille[row][column + i] 
        check_list.append(east_cell_content)

        if east_cell_content == player_piece and enemy_piece in check_list:
            another_check_list = []
            for index_transform in range(1, i):
                another_check_list.append(grille[row][column + index_transform])
            if '.' not in another_check_list:
                for index_transform in range(1, i):
                    grille [row, column + index_transform] = player_piece



# west_check = [grille[row][column - i]], row, column - i]
#         south_check = [grille[row + i][column]], row + i, column]
#         north_check = [grille[row  - i][column]], row - i, column]

## c'est qui etait au debut du main.py
# Grille d'Othello
# while True:
#     try:
#         taille = int(input(" Quelle taille de plateau voulez-vous ? Entrez une valeur paire, d'au moins 4 : "))
#         if taille >= 4 and taille % 2 == 0:
#             break
#         else:
#             print("Votre valeur n'est pas valide, entre en une autre.")
#     except:
#         print("Veuillez entrer un nombre entier...")

# grille = []
# for row in range(0, taille + 2):
#     grille.append([])
#     if row == 0:
#         grille[row].append(" ")
#         for column in range(1, taille + 2):
#             if column == taille + 1:
#                 grille[row].append("_")
#             else:
#                 grille[row].append(column)
#     elif row == taille + 1:
#         for column in range(1, taille + 2):
#             grille[row].append("_")
#     else:
#         grille[row].append(row)
#         for column in range(1, taille + 2):
#             if column == taille + 1:
#                 grille[row].append("_")
#             else:
#                 grille[row].append(".")

# grille = []
# for row in range(0, 10):
#     grille.append([])
#     if row == 0:
#         grille[row].append(" ")
#         for column in range(1, 10):
#             if column == 9:
#                 grille[row].append("_")
#             else:
#                 grille[row].append(column)
#     elif row == 9:
#         for column in range(1, 11):
#             grille[row].append("_")
#     else:
#         grille[row].append(row)
#         for column in range(1, 10):
#             if column == 9:
#                 grille[row].append("_")
#             else:
#                 grille[row].append(".")



## premier check autour

# def check_autour(row, column):
#     if row == 1 and column == 1: #NW corner
#         if grille[row][column + 1] == "." and grille[row + 1][column] == "." and grille[row + 1][column + 1] == ".":
#             return False
#     elif row == 1 and column == (len(grille[1]) - 1): #NE corner
#         if grille[row][column - 1] == "." and grille[row + 1][column] == "." and grille[row + 1][column - 1] == ".":
#             return False
#     elif row == (len(grille) - 1) and column == 1: #SW corner
#         if grille[row][column + 1] == "." and grille[row - 1][column] == "." and grille[row - 1][column + 1] == ".":
#             return False
#     elif row == (len(grille) - 1) and column == (len(grille[1]) - 1): #SE corner
#         if grille[row][column - 1] == "." and grille[row - 1][column] == "." and grille[row - 1][column - 1] == ".":
#             return False
#     elif row == 1: #N border
#         if grille[row][column - 1] == "." and grille[row][column + 1] == "." and grille[row + 1][column] == "." and grille[row + 1][column - 1] == "." and grille[row + 1][column + 1] == ".":
#             return False
#     elif column == 1:#W border
#         if grille[row][column + 1] == "." and grille[row - 1][column] == "." and grille[row + 1][column] == "." and grille[row - 1][column + 1] == "." and grille[row + 1][column + 1] == ".":
#             return False
#     elif row == (len(grille) - 1): #S border
#         if grille[row][column - 1] == "." and grille[row][column + 1] == "." and grille[row - 1][column] == "." and grille[row - 1][column + 1] == "." and grille[row - 1][column - 1] == ".":
#             return False
#     elif column == (len(grille[1]) - 1): #E border
#         if grille[row][column - 1] == "." and grille[row + 1][column] == "." and grille[row - 1][column] == "." and grille[row + 1][column - 1] == "." and grille[row - 1][column - 1] == ".":
#             return False
#     elif grille[row - 1][column] == "." and grille[row + 1][column] == "." and grille[row][column - 1] == "." and grille[row][column + 1] == "." and grille[row + 1][column - 1] == "." and grille[row + 1][column + 1] == "." and grille[row - 1][column - 1] == "." and grille[row - 1][column + 1] == ".":
#         return False
#     else:
#         return True






# ///////////////////////////////////////// NOS FONCTIONS RETURN /////////////////////////////////////////////////

# def return_x_vertical(grille, row_j2, column_j2):
#     check_table = []
#     for row_index in range(len(grille)):
#         if grille[row_index][column_j2] == "x" and row_index != row_j2 and "o" in check_table:
#                 if row_index < row_j2:
#                     for index_transform in range(row_index, row_j2 + 1):
#                         grille[index_transform][column_j2] = "x"
#                 else:
#                     for index_transform in range(row_j2, row_index + 1):
#                         grille[index_transform][column_j2] = "x"
#                 break
#     check_table.clear()

# def flip_o_diagonal(grille, row_j1, column_j1):
#     check_table = [] 
#     i = 0
#     #NW
#     while reached_limit(check_table, len(grille)) == False: # row of pion2 < row pion1
#         i+= 1
#         pion_2 = grille[row_j1 - i][column_j1 - i]
#         check_table.append(pion_2)
#         pion_2_position = (row_j1 - i, column_j1 - i)
#         if pion_2 == "o" and "x" in check_table:
#             for index_transform in range(1, (row_j1 - pion_2_position[0])):
#                 grille[row_j1 - index_transform][column_j1 - index_transform] = "o"
#     check_table.clear()
#     i = 0

#     #SE
#     while reached_limit(check_table, len(grille)) == False: # row of pion2 > row pion1
#         i+= 1
#         pion_2 = grille[row_j1 + i][column_j1 + i]
#         check_table.append(pion_2)
#         pion_2_position = (row_j1 + i, column_j1 + i)
#         if pion_2 == "o" and "x" in check_table:
#             for index_transform in range(1, (pion_2_position[0] - row_j1)):
#                 grille[row_j1 + index_transform][column_j1 + index_transform] = "o"
#     check_table.clear()
#     i = 0
    
#     #SW
#     while reached_limit(check_table, len(grille)) == False: # row of pion2 > row pion1
#         i+= 1
#         pion_2 = grille[row_j1 + i][column_j1 - i]
#         check_table.append(pion_2)
#         pion_2_position = (row_j1 + i, column_j1 - i)
#         if pion_2 == "o" and "x" in check_table:
#             for index_transform in range(1, (pion_2_position[0] - row_j1)):
#                 grille[row_j1 + index_transform][column_j1 - index_transform] = "o"
#     check_table.clear()
#     i = 0
#     #NE
#     while reached_limit(check_table, len(grille)) == False: # row of pion2 < row pion1
#         i+= 1
#         pion_2 = grille[row_j1 - i][column_j1 + i]
#         check_table.append(pion_2)
#         pion_2_position = (row_j1 - i, column_j1 + i)
#         if pion_2 == "o" and "x" in check_table:
#             for index_transform in range(1, (row_j1 - pion_2_position[0])):
#                 grille[row_j1 - index_transform][column_j1 + index_transform] = "o"
#     check_table.clear()
#     i = 0

# def flip_x_diagonal(grille, row_j2, column_j2):
#     check_table = [] 
#     i = 0
#     #NW
#     while reached_limit(check_table, len(grille)) == False: # row of pion2 < row pion1
#         i +=1
#         pion_2 = grille[row_j2 - i][column_j2 - i]
#         check_table.append(pion_2)
#         pion_2_position = (row_j2 - i, column_j2 - i)
#         if pion_2 == "x" and "o" in check_table:
#             for index_transform in range(1, (row_j2 - pion_2_position[0])):
#                 grille[row_j2 - index_transform][column_j2 - index_transform] = "x"    
#     check_table.clear()
#     i = 0
#     #SE
#     while reached_limit(check_table, len(grille)) == False: # row of pion2 > row pion1
#         i +=1
#         pion_2 = grille[row_j2 + i][column_j2 + i]
#         check_table.append(pion_2)
#         pion_2_position = (row_j2 + i, column_j2 + i)
#         if pion_2 == "x" and "o" in check_table:
#             for index_transform in range(1, (pion_2_position[0] - row_j2)):
#                 grille[row_j2 + index_transform][column_j2 + index_transform] = "x"
#     check_table.clear()
#     i = 0
#     #SW
#     while reached_limit(check_table, len(grille)) == False: # row of pion2 > row pion1
#         i +=1
#         pion_2 = grille[row_j2 + i][column_j2 - i]
#         check_table.append(pion_2)
#         pion_2_position = (row_j2 + i, column_j2 - i)
#         if pion_2 == "x" and "o" in check_table:
#             for index_transform in range(1, (pion_2_position[0] - row_j2)):
#                 grille[row_j2 + index_transform][column_j2 - index_transform] = "x"
#     check_table.clear()
#     i = 0
#     #NE
#     while reached_limit(check_table, len(grille)) == False: # row of pion2 < row pion1
#         i +=1
#         pion_2 = grille[row_j2 - i][column_j2 + i]
#         check_table.append(pion_2)
#         pion_2_position = (row_j2 - i, column_j2 + i)
#         if pion_2 == "x" and "o" in check_table:
#             for index_transform in range(1, (row_j2 - pion_2_position[0])):
#                 grille[row_j2 - index_transform][column_j2 + index_transform] = "x"
#     check_table.clear()
#     i = 0
