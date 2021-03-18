while True:
    column_j1 = int(input("Joueur 1, entrez la colonne : "))
    row_j1 = int(input("Joueur 1, entrez une ligne : "))
    break

print(column_j1)

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