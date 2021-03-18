#functions
import os


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

def reached_limit(liste_tour, length_matrix):
    if "|" in liste_tour or "_" in liste_tour or " " in liste_tour:
        return True
    length_index_list = [index for index in range(1, length_matrix - 1)]
    for element in length_index_list:
        if element in liste_tour:
            return True
    return False

def flip_horizontal(grille, player, row, column):
    if player == "player_1":
        player_piece = "o"
        enemy_piece = "x"
    elif player == "player_2":
        player_piece = "x"
        enemy_piece = "o"
    check_table = []
    i = 0
    while reached_limit(check_table, len(grille[1])) == False:
        i+= 1
        piece_2 = grille[row][column + i] # le pion qui va nous permettre de savoir s'il y a un autre pion de notre jour sur la meme ligne
        check_table.append(piece_2)

        piece_2_position = (row, column + i)
        if piece_2 == player_piece and enemy_piece in check_table:
            for index_transform in range(1, (piece_2_position[1] - column)):
                grille[row][column + index_transform] = player_piece
    check_table.clear()
    i = 0
    while reached_limit(check_table, len(grille[1])) == False:
        i+= 1
        piece_2 = grille[row][column - i]
        check_table.append(piece_2)
        piece_2_position = (row, column - i)
        if piece_2 == player_piece and enemy_piece in check_table:
            for index_transform in range(1, (column - piece_2_position[1])):
                grille[row][column - index_transform] = player_piece
    check_table.clear()
    i = 0

def flip_vertical(grille, player, row, column):
    if player == "player_1":
        player_piece = "o"
        enemy_piece = "x"
    elif player == "player_2":
        player_piece = "x"
        enemy_piece = "o"
    check_table = []
    i = 0
    while reached_limit(check_table, len(grille[1])) == False:
        i+= 1
        piece_2 = grille[row + i][column]
        check_table.append(piece_2)
        piece_2_position = (row + i, column)
        if piece_2 == player_piece and enemy_piece in check_table:
            for index_transform in range(1, (piece_2_position[0] - row)):
                grille[row + index_transform][column] = player_piece
    check_table.clear()
    i = 0
    while reached_limit(check_table, len(grille)) == False:
        i+= 1
        piece_2 = grille[row - i][column]
        check_table.append(piece_2)
        pion_2_position = (row - i, column)
        if piece_2 == player_piece and enemy_piece in check_table:
            for index_transform in range(1, (row - pion_2_position[0])):
                grille[row - index_transform][column] = player_piece
    check_table.clear()
    i = 0

def flip_o_diagonal(grille, row_j1, column_j1):
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
        pion_2 = grille[row_j1 + i][column_j1 - i]
        check_table.append(pion_2)
        pion_2_position = (row_j1 + i, column_j1 - i)
        if pion_2 == "o" and "x" in check_table:
            for index_transform in range(1, (pion_2_position[0] - row_j1)):
                grille[row_j1 + index_transform][column_j1 - index_transform] = "o"
    check_table.clear()
    i = 0
    #NE
    while reached_limit(check_table, len(grille)) == False: # row of pion2 < row pion1
        i+= 1
        pion_2 = grille[row_j1 - i][column_j1 + i]
        check_table.append(pion_2)
        pion_2_position = (row_j1 - i, column_j1 + i)
        if pion_2 == "o" and "x" in check_table:
            for index_transform in range(1, (row_j1 - pion_2_position[0])):
                grille[row_j1 - index_transform][column_j1 + index_transform] = "o"
    check_table.clear()
    i = 0

def flip_x_diagonal(grille, row_j2, column_j2):
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

def is_winner(grille):
    count_o = 0
    count_x = 0
    for row in grille:
        for element in row:
            if element == "o":
                count_o +=1
            elif element == "x":
                count_x += 1
    if count_o > count_x:
        print("Le joueur 1 a gagné 1️⃣!")
    elif count_o < count_x:
        print("Le joueur 2 a gagné 2️⃣!")
    else:
        print("Egalité 😳!")
