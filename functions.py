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
            another_checktable = []
            for index_transform in range(1, (piece_2_position[1] - column)):
                another_checktable.append(grille[row][column + index_transform])
            if '.' not in another_checktable:
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
            another_checktable = []
            for index_transform in range(1, (column - piece_2_position[1])):
                another_checktable.append(grille[row][column - index_transform])
            if '.' not in another_checktable:
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
