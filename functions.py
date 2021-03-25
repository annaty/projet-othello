#functions
import os
import math

def printGrille(grille_par):
    for element in grille_par:
        for truc in element:
            print(truc, end=" ")
        print()

# Fonction clear le terminal
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_autour(grille, row, column):
    if (grille[row - 1][column] != "x" and grille[row + 1][column] != "x" and grille[row][column - 1] != "x" 
            and grille[row][column + 1] != "x" and grille[row + 1][column - 1] != "x" and grille[row + 1][column + 1] != "x" 
            and grille[row - 1][column - 1] != "x" and grille[row - 1][column + 1] != "x" and grille[row - 1][column] != "o" 
            and grille[row + 1][column] != "o" and grille[row][column - 1] != "o" and grille[row][column + 1] != "o" 
            and grille[row + 1][column - 1] != "o" and grille[row + 1][column + 1] != "o" and grille[row - 1][column - 1] != "o" and grille[row - 1][column + 1] != "o"):
        return False
    else:
        return True

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

# def return_o_diagonal(grille, row_j1, column_j1):
#     check_table = [] 
#     if row_j1 < column_j1:
#         #NW
#         for i in range(1, column_j1): # row of pion2 < row pion1
#             pion_2 = grille[row_j1 - i][column_j1 - i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j1 - i, column_j1 - i)
#             if pion_2 == "o" and "x" in check_table:
#                 for index_transform in range(1, (row_j1 - pion_2_position[0])):
#                     grille[row_j1 - index_transform][column_j1 - index_transform] = "o"
#                 check_table.clear()

#         #SE
#         for i in range(1, len(grille) - column_j1): # row of pion2 > row pion1
#             pion_2 = grille[row_j1 + i][column_j1 + i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j1 + i, column_j1 + i)
#             if pion_2 == "o" and "x" in check_table:
#                 for index_transform in range(1, (pion_2_position[0] - row_j1)):
#                     grille[row_j1 + index_transform][column_j1 + index_transform] = "o"
#                 check_table.clear()
        
#         #SW
#         for i in range(-1, -(len(grille) - column_j1), -1): # row of pion2 > row pion1
#             pion_2 = grille[row_j1 - i][column_j1 + i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j1 - i, column_j1 + i)
#             if pion_2 == "o" and "x" in check_table:
#                 for index_transform in range(1, (pion_2_position[0] - row_j1)):
#                     grille[row_j1 + index_transform][column_j1 - index_transform] = "o"
#             check_table.clear()

#         #NE
#         for i in range(-1, len(grille) - column_j1, -1): # row of pion2 < row pion1
#             pion_2 = grille[row_j1 + i][column_j1 - i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j1 + i, column_j1 - i)
#             if pion_2 == "o" and "x" in check_table:
#                 for index_transform in range(1, (row_j1 - pion_2_position[0])):
#                     grille[row_j1 - index_transform][column_j1 + index_transform] = "o"
#             check_table.clear()

#     else:
#         for i in range(1, row_j1): # row of pion2 < row pion1
#             pion_2 = grille[row_j1 - i][column_j1 - i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j1 - i, column_j1 - i)
#             if pion_2 == "o" and "x" in check_table:
#                 for index_transform in range(1, (row_j1 - pion_2_position[0])):
#                     grille[row_j1 - index_transform][column_j1 - index_transform] = "o"
#                 check_table.clear()

#         #SE
#         for i in range(1, len(grille) - row_j1): # row of pion2 > row pion1
#             pion_2 = grille[row_j1 + i][column_j1 + i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j1 + i, column_j1 + i)
#             if pion_2 == "o" and "x" in check_table:
#                 for index_transform in range(1, (pion_2_position[0] - row_j1)):
#                     grille[row_j1 + index_transform][column_j1 + index_transform] = "o"
#                 check_table.clear()
        
#         #SW
#         for i in range(-1, -(len(grille) - row_j1), -1): # row of pion2 > row pion1
#             pion_2 = grille[row_j1 - i][column_j1 + i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j1 - i, column_j1 + i)
#             if pion_2 == "o" and "x" in check_table:
#                 for index_transform in range(1, (pion_2_position[0] - row_j1)):
#                     grille[row_j1 + index_transform][column_j1 - index_transform] = "o"
#             check_table.clear()

#         #NE
#         for i in range(-1, len(grille) - row_j1, -1): # row of pion2 < row pion1
#             pion_2 = grille[row_j1 + i][column_j1 - i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j1 + i, column_j1 - i)
#             if pion_2 == "o" and "x" in check_table:
#                 for index_transform in range(1, (row_j1 - pion_2_position[0])):
#                     grille[row_j1 - index_transform][column_j1 + index_transform] = "o"
#             check_table.clear()


# def return_x_diagonal(grille, row_j2, column_j2):
#     check_table = [] 
#     if row_j2 < column_j2:
#         #NW
#         for i in range(1, row_j2): # row of pion2 < row pion1
#             pion_2 = grille[row_j2 - i][column_j2 - i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 - i, column_j2 - i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (row_j2 - pion_2_position[0])):
#                     grille[row_j2 - index_transform][column_j2 - index_transform] = "x"
#                 check_table.clear()

#         #SE
#         for i in range(1, len(grille) - row_j2): # row of pion2 > row pion1
#             pion_2 = grille[row_j2 + i][column_j2 + i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 + i, column_j2 + i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (pion_2_position[0] - row_j2)):
#                     grille[row_j2 + index_transform][column_j2 + index_transform] = "x"
#                 check_table.clear()
        
#         #SW
#         for i in range(1, len(grille) - column_j2): # row of pion2 > row pion1
#             pion_2 = grille[row_j2 + i][column_j2 - i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 + i, column_j2 - i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (pion_2_position[0] - row_j2)):
#                     grille[row_j2 + index_transform][column_j2 - index_transform] = "x"
#                 check_table.clear()

#         #NE
#         for i in range(1, len(grille[1]) - column_j2): # row of pion2 < row pion1
#             pion_2 = grille[row_j2 - i][column_j2 + i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 - i, column_j2 + i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (row_j2 - pion_2_position[0])):
#                     grille[row_j2 - index_transform][column_j2 + index_transform] = "x"
#                 check_table.clear()

#     elif row_j2 > column_j2 :
#         #NW
#         for i in range(1, column_j2): # row of pion2 < row pion1
#             pion_2 = grille[row_j2 - i][column_j2 - i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 - i, column_j2 - i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (row_j2 - pion_2_position[0])):
#                     grille[row_j2 - index_transform][column_j2 - index_transform] = "x"
#                 check_table.clear()

#         #SE
#         for i in range(1, len(grille) - row_j2): # row of pion2 > row pion1
#             pion_2 = grille[row_j2 + i][column_j2 + i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 + i, column_j2 + i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (pion_2_position[0] - row_j2)):
#                     grille[row_j2 + index_transform][column_j2 + index_transform] = "x"
#                 check_table.clear()
        
#         #SW
#         for i in range(1, column_j2): # row of pion2 > row pion1
#             pion_2 = grille[row_j2 + i][column_j2 - i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 + i, column_j2 - i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (pion_2_position[0] - row_j2)):
#                     grille[row_j2 + index_transform][column_j2 - index_transform] = "x"
#                 check_table.clear()

#         #NE
#         for i in range(1, len(grille[1]) - column_j2): # row of pion2 < row pion1
#             pion_2 = grille[row_j2 - i][column_j2 + i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 - i, column_j2 + i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (row_j2 - pion_2_position[0])):
#                     grille[row_j2 - index_transform][column_j2 + index_transform] = "x"
#                 check_table.clear()

#     elif row_j2 == column_j2 and row_j2 < len(grille) / 2:
#         #NW
#         for i in range(1, row_j2): # row of pion2 < row pion1
#             pion_2 = grille[row_j2 - i][column_j2 - i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 - i, column_j2 - i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (row_j2 - pion_2_position[0])):
#                     grille[row_j2 - index_transform][column_j2 - index_transform] = "x"
#                 check_table.clear()

#         #SE
#         for i in range(1, len(grille) - row_j2): # row of pion2 > row pion1
#             pion_2 = grille[row_j2 + i][column_j2 + i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 + i, column_j2 + i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (pion_2_position[0] - row_j2)):
#                     grille[row_j2 + index_transform][column_j2 + index_transform] = "x"
#                 check_table.clear()
        
#         #SW
#         for i in range(1, row_j2 - 1): # row of pion2 > row pion1
#             pion_2 = grille[row_j2 + i][column_j2 - i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 + i, column_j2 - i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (pion_2_position[0] - row_j2)):
#                     grille[row_j2 + index_transform][column_j2 - index_transform] = "x"
#                 check_table.clear()

#         #NE
#         for i in range(1, row_j2 - 1): # row of pion2 < row pion1
#             pion_2 = grille[row_j2 - i][column_j2 + i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 - i, column_j2 + i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (row_j2 - pion_2_position[0])):
#                     grille[row_j2 - index_transform][column_j2 + index_transform] = "x"
#                 check_table.clear()

#     elif row_j2 == column_j2 and row_j2 > len(grille) / 2:
#         #NW
#         for i in range(1, math.floor(row_j2 / 2)): # row of pion2 < row pion1
#             pion_2 = grille[row_j2 - i][column_j2 - i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 - i, column_j2 - i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (row_j2 - pion_2_position[0])):
#                     grille[row_j2 - index_transform][column_j2 - index_transform] = "x"
#                 check_table.clear()

#         #SE
#         for i in range(1, len(grille) - row_j2): # row of pion2 > row pion1
#             pion_2 = grille[row_j2 + i][column_j2 + i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 + i, column_j2 + i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (pion_2_position[0] - row_j2)):
#                     grille[row_j2 + index_transform][column_j2 + index_transform] = "x"
#                 check_table.clear()
        
#         #SW
#         for i in range(1, len(grille) - row_j2): # row of pion2 > row pion1
#             pion_2 = grille[row_j2 + i][column_j2 - i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 + i, column_j2 - i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (pion_2_position[0] - row_j2)):
#                     grille[row_j2 + index_transform][column_j2 - index_transform] = "x"
#                 check_table.clear()

#         #NE
#         for i in range(1, math.floor((row_j2 / 2 - 1))): # row of pion2 < row pion1
#             pion_2 = grille[row_j2 - i][column_j2 + i]
#             check_table.append(pion_2)
#             pion_2_position = (row_j2 - i, column_j2 + i)
#             if pion_2 == "x" and "o" in check_table:
#                 for index_transform in range(1, (row_j2 - pion_2_position[0])):
#                     grille[row_j2 - index_transform][column_j2 + index_transform] = "x"
#                 check_table.clear()

def reached_limit(list, length_matrix):
    if "|" in list or "_" in list or " " in list:
        return True
    length_index_list = [index for index in range(0, length_matrix)]
    for element in length_index_list:
        if element in list:
            return True
    return False

def return_o_diagonal(grille, row_j1, column_j1):
    check_table = [] 
    i = 0
    #NW
    while reached_limit(check_table, len(grille)) == False: # row of pion2 < row pion1
        i+= 1
        pion_2 = grille[row_j1 - i][column_j1 - i]
        check_table.append(pion_2)
        pion_2_position = (row_j1 - i, column_j1 - i)
        if pion_2 == "o" and "x" in check_table:
            for index_transform in range(1, (row_j1 - pion_2_position[0])):
                grille[row_j1 - index_transform][column_j1 - index_transform] = "o"
    check_table.clear()
    i = 0

    #SE
    while reached_limit(check_table, len(grille)) == False: # row of pion2 > row pion1
        i+= 1
        pion_2 = grille[row_j1 + i][column_j1 + i]
        check_table.append(pion_2)
        pion_2_position = (row_j1 + i, column_j1 + i)
        if pion_2 == "o" and "x" in check_table:
            for index_transform in range(1, (pion_2_position[0] - row_j1)):
                grille[row_j1 + index_transform][column_j1 + index_transform] = "o"
    check_table.clear()
    i = 0
    
    #SW
    while reached_limit(check_table, len(grille)) == False: # row of pion2 > row pion1
        i+= 1
        pion_2 = grille[row_j1 - i][column_j1 + i]
        check_table.append(pion_2)
        pion_2_position = (row_j1 - i, column_j1 + i)
        if pion_2 == "o" and "x" in check_table:
            for index_transform in range(1, (pion_2_position[0] - row_j1)):
                grille[row_j1 + index_transform][column_j1 - index_transform] = "o"
    check_table.clear()
    i = 0
    #NE
    while reached_limit(check_table, len(grille)) == False: # row of pion2 < row pion1
        i+= 1
        pion_2 = grille[row_j1 + i][column_j1 - i]
        check_table.append(pion_2)
        pion_2_position = (row_j1 + i, column_j1 - i)
        if pion_2 == "o" and "x" in check_table:
            for index_transform in range(1, (row_j1 - pion_2_position[0])):
                grille[row_j1 - index_transform][column_j1 + index_transform] = "o"
    check_table.clear()
    i = 0

def return_x_diagonal(grille, row_j2, column_j2):
    check_table = [] 
    i = 0
    #NW
    while reached_limit(check_table, len(grille)) == False: # row of pion2 < row pion1
        i +=1
        pion_2 = grille[row_j2 - i][column_j2 - i]
        check_table.append(pion_2)
        pion_2_position = (row_j2 - i, column_j2 - i)
        if pion_2 == "x" and "o" in check_table:
            for index_transform in range(1, (row_j2 - pion_2_position[0])):
                grille[row_j2 - index_transform][column_j2 - index_transform] = "x"    
    check_table.clear()
    i = 0
    #SE
    while reached_limit(check_table, len(grille)) == False: # row of pion2 > row pion1
        i +=1
        pion_2 = grille[row_j2 + i][column_j2 + i]
        check_table.append(pion_2)
        pion_2_position = (row_j2 + i, column_j2 + i)
        if pion_2 == "x" and "o" in check_table:
            for index_transform in range(1, (pion_2_position[0] - row_j2)):
                grille[row_j2 + index_transform][column_j2 + index_transform] = "x"
    check_table.clear()
    i = 0
    #SW
    while reached_limit(check_table, len(grille)) == False: # row of pion2 > row pion1
        i +=1
        pion_2 = grille[row_j2 + i][column_j2 - i]
        check_table.append(pion_2)
        pion_2_position = (row_j2 + i, column_j2 - i)
        if pion_2 == "x" and "o" in check_table:
            for index_transform in range(1, (pion_2_position[0] - row_j2)):
                grille[row_j2 + index_transform][column_j2 - index_transform] = "x"
    check_table.clear()
    i = 0
    #NE
    while reached_limit(check_table, len(grille)) == False: # row of pion2 < row pion1
        i +=1
        pion_2 = grille[row_j2 - i][column_j2 + i]
        check_table.append(pion_2)
        pion_2_position = (row_j2 - i, column_j2 + i)
        if pion_2 == "x" and "o" in check_table:
            for index_transform in range(1, (row_j2 - pion_2_position[0])):
                grille[row_j2 - index_transform][column_j2 + index_transform] = "x"
    check_table.clear()
    i = 0

    # for i in range(1, 2):
    #     if grille[row_j1 + i][column_j1 + i] == "o": # SE
    #         for index_transform in range(1, i):
    #             grille[row_j1 + i][column_j1 + i] = "o"
    #     elif grille[row_j1 - i][column_j1 - i] == "o": # NO
    #         for index_transform in range(1, i):
    #             grille[row_j1 - i][column_j1 - i] = "o"
    #     elif grille[row_j1 + i][column_j1 - i] == "o": # SO
    #         for index_transform in range(1, i):
    #             grille[row_j1 + i][column_j1 - i] = "o"
    #     elif grille[row_j1 - i][column_j1 + i] == "o": # NE
    #         for index_transform in range(1, i):
    #             grille[row_j1 - i][column_j1 + i] = "o"