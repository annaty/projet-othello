<<<<<<< HEAD
#functions
import os
<<<<<<< HEAD
import math
=======
>>>>>>> 1ed0b9e920e02b0d08a9f97a5d2e8af166034420

def printGrille(grille_par):
    for element in grille_par:
        for truc in element:
            print(truc, end=" ")
        print()

# Fonction clear le terminal
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

<<<<<<< HEAD

=======
>>>>>>> 1ed0b9e920e02b0d08a9f97a5d2e8af166034420
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
    if player == "Joueur 1":
        player_piece = "o"
        enemy_piece = "x"
    elif player == "Joueur 2":
        player_piece = "x"
        enemy_piece = "o"
    check_table = []
    i = 0
    while reached_limit(check_table, len(grille[1])) == False:
        i+= 1
        piece_2 = grille[row][column + i] # le pion qui va nous permettre de savoir s'il y a un autre pion de notre joueur sur la meme ligne
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
    if player == "Joueur 1":
        player_piece = "o"
        enemy_piece = "x"
    elif player == "Joueur 2":
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
        piece_2_position = (row - i, column)
        if piece_2 == player_piece and enemy_piece in check_table:
            for index_transform in range(1, (row - piece_2_position[0])):
                grille[row - index_transform][column] = player_piece
    check_table.clear()
    i = 0

def flip_diagonal(grille, player, row, column):
    if player == "Joueur 1":
        player_piece = "o"
        enemy_piece = "x"
    elif player == "Joueur 2":
        player_piece = "x"
        enemy_piece = "o"
    check_table=[]
    i = 0

    #NW
    while reached_limit(check_table, len(grille)) == False:
        i+= 1
        piece_2 = grille[row - i][column - i]
        check_table.append(piece_2)
        piece_2_position = (row - i, column - i)
        if piece_2 == player_piece and enemy_piece in check_table:
            for index_transform in range (1, row - piece_2_position[0]):
                grille[row - index_transform][column - index_transform] = player_piece
    check_table.clear()
    i = 0

    #SE
    while reached_limit(check_table, len(grille)) == False:
        i+= 1
        piece_2 = grille[row + i][column + i]
        print(piece_2)
        check_table.append(piece_2)
        piece_2_position = (row + i, column + i)
        if piece_2 == player_piece and enemy_piece in check_table:
            for index_transform in range(1, (piece_2_position[0] - row)):
                grille[row + index_transform][column + index_transform] = player_piece
    check_table.clear()
    i = 0

    #SW
    while reached_limit(check_table, len(grille)) == False:
        i+= 1
        piece_2 = grille[row + i][column - i]
        check_table.append(piece_2)
        piece_2_position = (row + i, column - i)
        if piece_2 == player_piece and enemy_piece in check_table:
            for index_transform in range(1, (piece_2_position[0] - row)):
                grille[row + index_transform][column - index_transform] = player_piece
    check_table.clear()
    i = 0

    #NE
    while reached_limit(check_table, len(grille)) == False: # row of pion2 < row pion1
        i+= 1
        piece_2 = grille[row - i][column + i]
        check_table.append(piece_2)
        piece_2_position = (row - i, column + i)
        if piece_2 == player_piece and enemy_piece in check_table:
            for index_transform in range(1, (row - piece_2_position[0])):
                grille[row - index_transform][column + index_transform] = player_piece
    check_table.clear()
    i = 0

def user_move(grille, player):
    if player == "Joueur 1":
        player_piece = "o"
    elif player == "Joueur 2":
        player_piece = "x"
    while True:
        while True:
            column = input("{}, entrez la colonne : ".format(player))
            try:
                column = int(column)
                break
            except:
                print("Saisie non valide...")
        while True:
            row = input("{}, entrez une ligne : ".format(player))
            try:
                row = int(row)
                break
            except:
                print("Saisie non valide...")

        if 1 <= column <= 8 and 1 <= row <= 8:
            if check_autour(grille, row, column) and grille[row][column] == ".":
                grille[row][column] = player_piece
                break
            else:
                print("Placement non autorisé... Regardez les regles du jeu, merci.")
        else:
            print("Placement non autorisé... Regardez les regles du jeu, merci.")
    return row, column


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
=======
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

def reached_limit(liste_champs, length_matrix):
    if "|" in liste_champs or "_" in liste_champs or " " in liste_champs:
        return True
    length_index_list = [index for index in range(1, length_matrix - 1)]
    for element in length_index_list:
        if element in liste_champs:
            return True
    return False

def color_assignment(player):
    if player == "Joueur 1":
        return 'o', 'x'
    elif player == "Joueur 2":
        return 'x', 'o'

def flip_horizontal(grille, player, row, column):
    player_piece, enemy_piece = color_assignment(player)
    check_list = [] # une liste qui contient le contenu de toutes les cellules dans la direction donnée, en partant de la pièce que l'on pose, jusqu'au bord
    i = 0 # une variable utilisée pour suivre le nombre d'itérations de la boucle

    #Eastern check
    while reached_limit(check_list, len(grille)) == False:
        i+= 1
        east_cell_content = grille[row][column + i]
        check_list.append(east_cell_content)
        if east_cell_content == player_piece and (enemy_piece in check_list) and ('.' not in check_list):
            for index_transform in range(1, i + 1):
                grille[row][column + index_transform] = player_piece
    check_list.clear()
    i = 0

    #Western check
    while reached_limit(check_list, len(grille)) == False:
        i+= 1
        west_cell_content = grille[row][column - i]
        check_list.append(west_cell_content)
        if west_cell_content == player_piece and (enemy_piece in check_list) and ('.' not in check_list):
            for index_transform in range(1, i + 1):
                grille[row][column - index_transform] = player_piece

def flip_vertical(grille, player, row, column):
    player_piece, enemy_piece = color_assignment(player)
    check_list = []
    i = 0

    #Southern check
    while reached_limit(check_list, len(grille)) == False:
        i+= 1
        south_cell_content = grille[row + i][column]
        check_list.append(south_cell_content)
        if south_cell_content == player_piece and (enemy_piece in check_list) and ('.' not in check_list):
                for index_transform in range(1, i + 1):
                    grille[row + index_transform][column] = player_piece
    check_list.clear()
    i = 0

    #Northern check
    while reached_limit(check_list, len (+grille)) == False:
        i+= 1
        north_cell_content = grille[row - i][column]
        check_list.append(north_cell_content)
        if north_cell_content == player_piece and (enemy_piece in check_list) and ('.' not in check_list):
            for index_transform in range(1, i + 1):
                grille[row - index_transform][column] = player_piece

def flip_diagonal(grille, player, row, column):
    player_piece, enemy_piece = color_assignment(player)
    check_list=[]
    i = 0

    #NW check
    while reached_limit(check_list, len(grille)) == False:
        i += 1
        nw_cell_content = grille[row - i][column - i]
        check_list.append(nw_cell_content)
        if nw_cell_content == player_piece and (enemy_piece in check_list) and ('.' not in check_list):
            for index_transform in range (1, i + 1):
                grille[row - index_transform][column - index_transform] = player_piece
    check_list.clear()
    i = 0

    #SE check
    while reached_limit(check_list, len(grille)) == False:
        i+= 1
        se_cell_content = grille[row + i][column + i]
        check_list.append(se_cell_content)
        if se_cell_content == player_piece and (enemy_piece in check_list) and ('.' not in check_list):
            for index_transform in range(1, i + 1):
                grille[row + index_transform][column + index_transform] = player_piece
    check_list.clear()
    i = 0

    #SW check
    while reached_limit(check_list, len(grille)) == False:
        i+= 1
        sw_cell_content = grille[row + i][column - i]
        check_list.append(sw_cell_content)
        if sw_cell_content== player_piece and (enemy_piece in check_list) and ('.' not in check_list):
            for index_transform in range(1, i + 1):
                grille[row + index_transform][column - index_transform] = player_piece
    check_list.clear()
    i = 0

    #NE check
    while reached_limit(check_list, len(grille)) == False:
        i+= 1
        ne_cell_content = grille[row - i][column + i]
        check_list.append(ne_cell_content)
        if ne_cell_content == player_piece and (enemy_piece in check_list) and ('.' not in check_list):
            for index_transform in range(1, i + 1):
                grille[row - index_transform][column + index_transform] = player_piece

def user_move(grille, player):
    player_piece, enemy_piece = color_assignment(player)
    while True:
        while True:
            column = input("{}, entrez la colonne : ".format(player))
            try:
                column = int(column)
                break
            except:
                print("Saisie non valide...")
        while True:
            row = input("{}, entrez une ligne : ".format(player))
            try:
                row = int(row)
                break
            except:
                print("Saisie non valide...")

        if 1 <= column <= 8 and 1 <= row <= 8:
            if check_autour(grille, row, column) and grille[row][column] == ".":
                grille[row][column] = player_piece
                break
            else:
                print("Placement non autorisé... Regardez les regles du jeu, merci.")
        else:
            print("Placement non autorisé... Regardez les regles du jeu, merci.")
    return row, column


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
>>>>>>> 2b4ce033c76fd71181059b23d2f28d6c442c334c
