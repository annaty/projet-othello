<<<<<<< HEAD
while True:
    column_j1 = int(input("Joueur 1, entrez la colonne : "))
    row_j1 = int(input("Joueur 1, entrez une ligne : "))
    break

print(column_j1)
=======
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
>>>>>>> 1ed0b9e920e02b0d08a9f97a5d2e8af166034420

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
<<<<<<< HEAD
=======






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
>>>>>>> 1ed0b9e920e02b0d08a9f97a5d2e8af166034420
