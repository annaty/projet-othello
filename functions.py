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
    while reached_limit(check_list, len (grille)) == False:
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
