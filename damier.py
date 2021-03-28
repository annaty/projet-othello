from math import *
# o --> bleu
# x --> rouge
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
class Damier():
    def __init__(self, canevas):
        self.can = canevas
        self.lesCases = []
        self.move_counter = 1

        #end screen variables
        self.grille_size = 0
        self.fullboard_state = BooleanVar()
        self.board_state = self.fullboard_state.get()
        self.winner = StringVar()

        #tkinter variables
        self.p1_var_int = IntVar(value=0)
        self.p2_var_int = IntVar(value=0)
        self.p1_var_str = StringVar()
        self.p2_var_str = StringVar()
        self.p1_var_str.set(value=self.p1_var_int.get())
        self.p2_var_str.set(value=self.p2_var_int.get())
        self.current_player = StringVar(value='Blanc')

    def creation_grille(self, taille):
        self.grille_size = taille
        grille = []
        y1 = 10
        y2 = y1 + 30
        for ligne in range(0, taille + 2):
            x1 = 10
            x2 = x1 + 30
            self.lesCases.append([])
            if ligne == taille + 1:
                for colonne in range(0,taille):
                    self.lesCases[ligne].append("_")
            elif ligne == 0:
                for colonne in range(0,taille + 1):
                    if colonne == 0:
                        self.lesCases[ligne].append(" ")
                    else:
                        self.lesCases[ligne].append(colonne)
            else :
                for colonne in range(0 ,taille + 2):
                    if colonne == taille + 1:
                        self.lesCases[ligne].append("_")
                    elif colonne == 0:
                        self.lesCases[ligne].append(ligne)
                    else:
                        x1 += 30
                        x2 += 30
                        self.lesCases[ligne].append([(x1,x2), (y1,y2), False, " "])
            y1 += 30
            y2 = y1 + 30
        y1 = 10
        y2 = y1 + 30
        for row in range(0, taille + 2):
            grille.append([])
            x1 = 10
            x2 = x1 + 30
            if row == 0: #premier ligne
                grille[row].append(" ")
                self.can.create_rectangle(x1, y1, x2, y2, outline='light steel blue') # top left corner
                
                for column in range(1, taille + 2):
                    if column == taille + 1:
                        grille[row].append('_')
                        
                    else:
                        x1 += 30
                        x2 += 30
                        grille[row].append(column)
                        self.can.create_rectangle(x1, y1, x2, y2, outline='light steel blue')
                        self.can.create_text(x1+15, y1+15, text = column)
                        
            elif row == taille + 1: # derniere ligne
                grille[row].append(" ")
                
                for column in range(1, taille + 2):
                    if column == taille + 1: # derniere colonne
                        grille[row].append('_')
                        
                    else:
                        x1 += 30
                        x2 += 30
                        grille[row].append(column)
                        
            else: # autres lignes
                grille[row].append(row)
                self.can.create_rectangle(x1, y1, x2, y2, outline='light steel blue')
                self.can.create_text(x1 +15, y1 + 15, text = grille[row][0])
                
                x1 += 30
                x2 += 30
                for column in range(1, taille + 2):
                    if column == taille + 1:
                        
                        grille[row].append("_")
                    else:
                        grille[row].append(".")
                        self.can.create_rectangle(x1, y1, x2, y2, outline='gray50')
                        
                        x1 += 30
                        x2 += 30
                    
            y1 += 30
            y2 += 30
            
        #=============   position de depart   =======================
        milieu = int(floor(len(grille)*30-10) / 2)
        milieu_colonne = int(floor(len(grille[0])*30-10) / 2)

        milieu_table = int(floor(len(self.lesCases) - 2) / 2)
        padd = 2
        
        self.can.create_oval(milieu + padd + 15, milieu + padd + 15, milieu + 28 + 15 , milieu + 28 + 15, fill='snow', outline='snow')
        # self.lesCases.remove([(milieu + 15, milieu + 30 + 15),(milieu + 15, milieu + 30 + 15), False, ""])
        self.lesCases[milieu_table + 1][milieu_table + 1] = [(milieu + 15, milieu + 30 + 15),(milieu_colonne + 15, milieu_colonne + 30 + 15), True, "snow"]

        self.can.create_oval(milieu + padd - 15, milieu + padd - 15, milieu + 28 - 15 , milieu + 28 - 15, fill='snow', outline='snow')
        # self.lesCases.remove([(milieu - 15, milieu + 30 - 15),(milieu - 15, milieu + 30 - 15), False, ""])
        self.lesCases[milieu_table][milieu_table] = [(milieu - 15, milieu + 30 - 15),(milieu_colonne - 15, milieu_colonne + 30 - 15), True, "snow"]

        self.can.create_oval(milieu + padd + 15,  milieu + padd - 15, milieu + 28 + 15 , milieu + 28 - 15, fill='gray24', outline='gray24')
        # self.lesCases.remove([(milieu + 15, milieu + 30 + 15),(milieu - 15, milieu + 30 - 15), False, ""])
        self.lesCases[milieu_table][milieu_table + 1] = [(milieu + 15, milieu + 30 + 15),(milieu_colonne - 15, milieu_colonne + 30 - 15), True, "gray24"]

        self.can.create_oval(milieu + padd - 15, milieu + padd + 15, milieu + 28 - 15 , milieu + 28 + 15, fill='gray24', outline='gray24')
        # self.lesCases.remove([(milieu - 15, milieu + 30 - 15),(milieu + 15, milieu + 30 + 15), False, ""])
        self.lesCases[milieu_table + 1][milieu_table] = [(milieu - 15, milieu + 30 - 15),(milieu_colonne + 15, milieu_colonne + 30 + 15), True, "gray24"]

        self.p1_var_int.set(value=2)
        self.p2_var_int.set(value=2)

    def check_autour(self, laLigne, laCase):
        case_counter = 0
        try :
            if self.lesCases[self.lesCases.index(laLigne)][laLigne.index(laCase) + 1][2] == False:       # Case DROITE
                case_counter += 1
        except:
            case_counter += 1
        try:
            if self.lesCases[self.lesCases.index(laLigne)][laLigne.index(laCase) - 1][2] == False:        # Case GAUCHE
                case_counter += 1
        except:
            case_counter +=1        
        try:
            if self.lesCases[self.lesCases.index(laLigne) - 1][laLigne.index(laCase)][2] == False:        # Case HAUT
                case_counter += 1
        except:
            case_counter +=1        
        try:
            if self.lesCases[self.lesCases.index(laLigne) + 1][laLigne.index(laCase)][2] == False:        # Case BAS 
                case_counter += 1
        except:
            case_counter +=1        
        try:
            if self.lesCases[self.lesCases.index(laLigne) - 1][laLigne.index(laCase) + 1][2] == False:        # Case diag DROITE HAUT
                case_counter += 1
        except:
            case_counter +=1        
        try:
            if self.lesCases[self.lesCases.index(laLigne) + 1][laLigne.index(laCase) + 1][2] == False:        # Case diag DROITE BAS
                case_counter += 1
        except:
            case_counter +=1        
        try:
            if self.lesCases[self.lesCases.index(laLigne) - 1][laLigne.index(laCase) - 1][2] == False:        # Case diag GAUCHE HAUT
                case_counter += 1
        except:
            case_counter +=1        
        try:
            if self.lesCases[self.lesCases.index(laLigne) + 1][laLigne.index(laCase) - 1][2] == False:        # Case diag GAUCHE BAS
                case_counter += 1
        except:
            case_counter +=1        
                
        return not case_counter == 8

    def check_valid_position(self, x, y):
        return (40 < x < (40 + 30 * 8) and 40 < y < (40 + 30 * 8))
    
    def color_assignment(self, pion_joue):
        if pion_joue == "snow": #Joueur 1
            return 'snow', 'gray24'
        elif pion_joue == "gray24": #Joueur 2
            return 'gray24', 'snow'
    
    def reached_limit(self, liste_champs, length_matrix):
        if "|" in liste_champs or "_" in liste_champs or " " in liste_champs:
            return True
        length_index_list = [index for index in range(1, length_matrix - 1)]
        for element in length_index_list:
            if element in liste_champs:
                return True
        return False


    def flip_horizontal(self, grille, player, row, column, placement):
        #on mentionne la position du piont que l'on vient de poser
        player_piece, enemy_piece = self.color_assignment(player)
        check_list = [] # une liste qui contient le contenu de toutes les cellules dans la direction donnée, en partant de la pièce que l'on pose, jusqu'au bord
        i = 0 # une variable utilisée pour suivre le nombre d'itérations de la boucle
        #Eastern check
        try:
            while self.reached_limit(check_list, len(grille)) == False:
                i+= 1
                east_cell_content = grille[row][column + i][3]
                check_list.append(east_cell_content)
                if east_cell_content == player_piece and (enemy_piece in check_list):
                    for index_transform in range(1, i + 1):
                        if placement == "placement":
                            return True
                        else:
                            grille[row][column + index_transform][3] = player_piece
                print("tour east", check_list)
        except:
            pass
            
        check_list.clear()
        i = 0

        #Western check
        try:
            while self.reached_limit(check_list, len(grille)) == False:
                i+= 1
                west_cell_content = grille[row][column - i][3]
                check_list.append(west_cell_content)
                if west_cell_content == player_piece and (enemy_piece in check_list):
                    for index_transform in range(1, i + 1):
                        if placement == "placement":
                            return True
                        else:
                            grille[row][column - index_transform][3] = player_piece
        except:
            pass

    def flip_vertical(self, grille, player, row, column, placement):
        player_piece, enemy_piece = self.color_assignment(player)
        check_list = []
        i = 0

        #Southern check
        try:
            while self.reached_limit(check_list, len(grille)) == False:
                i+= 1
                south_cell_content = grille[row + i][column][3]
                check_list.append(south_cell_content)
                if south_cell_content == player_piece and (enemy_piece in check_list) and ('.' not in check_list):
                    for index_transform in range(1, i + 1):
                        if placement == "placement":
                            return True
                        else:
                            grille[row + index_transform][column][3] = player_piece
                        print("tour west", check_list)
        except:
            # print("problem south")
            pass
        check_list.clear()
        i = 0

        #Northern check
        try:
            while self.reached_limit(check_list, len(grille)) == False:
                i+= 1
                north_cell_content = grille[row - i][column][3]
                check_list.append(north_cell_content)
                if north_cell_content == player_piece and (enemy_piece in check_list) and ('.' not in check_list):
                    for index_transform in range(1, i + 1):
                        if placement == "placement":
                            return True
                        else:
                            grille[row - index_transform][column][3] = player_piece
                        print("tour west", check_list)
        except:
            # print("problem north")
            pass


    def flip_diagonal(self, grille, player, row, column, placement):
        player_piece, enemy_piece = self.color_assignment(player)
        check_list=[]
        i = 0

        #NW check
        try:
            while self.reached_limit(check_list, len(grille)) == False:
                i += 1
                nw_cell_content = grille[row - i][column - i][3]
                check_list.append(nw_cell_content)
                if nw_cell_content == player_piece and (enemy_piece in check_list) and ('.' not in check_list):
                    for index_transform in range (1, i + 1):
                        if placement == "placement":
                            return True
                        else:
                            grille[row - index_transform][column - index_transform][3] = player_piece
        except:
            pass
        check_list.clear()
        i = 0

        #SE check
        try:
            while self.reached_limit(check_list, len(grille)) == False:
                i+= 1
                se_cell_content = grille[row + i][column + i][3]
                check_list.append(se_cell_content)
                if se_cell_content == player_piece and (enemy_piece in check_list) and ('.' not in check_list):
                    for index_transform in range(1, i + 1):
                        if placement == "placement":
                            return True
                        else:
                            grille[row + index_transform][column + index_transform][3] = player_piece
        except:
            pass
        check_list.clear()
        i = 0

        #SW check
        try:
            while self.reached_limit(check_list, len(grille)) == False:
                i+= 1
                sw_cell_content = grille[row + i][column - i][3]
                check_list.append(sw_cell_content)
                if sw_cell_content== player_piece and (enemy_piece in check_list) and ('.' not in check_list):
                    for index_transform in range(1, i + 1):
                        if placement == "placement":
                            return True
                        else:
                            grille[row + index_transform][column - index_transform][3] = player_piece
        except:
            pass
        check_list.clear()
        i = 0

        #NE check
        try:
            while self.reached_limit(check_list, len(grille)) == False:
                i+= 1
                ne_cell_content = grille[row - i][column + i][3]
                check_list.append(ne_cell_content)
                if ne_cell_content == player_piece and (enemy_piece in check_list) and ('.' not in check_list):
                    for index_transform in range(1, i + 1):
                        if placement == "placement":
                            return True
                        else:
                            grille[row - index_transform][column + index_transform][3] = player_piece
        except:
            pass

    def posePion(self, event):
        x = event.x
        y = event.y
        print(self.grille_size)

        for ligne in self.lesCases:
            for case in ligne:
                if self.move_counter % 2 == 0:
                    couleur = 'gray24'
                    self.current_player.set(value='Noir')
                elif self.move_counter % 2 == 1:
                    couleur = 'snow'    
                    self.current_player.set(value='Blanc')
                try:
                    if ((case[0][0] < x < case[0][1]) and (case[1][0] < y < case[1][1])) and (case[2] == False):
                        if self.flip_horizontal(self.lesCases, couleur, self.lesCases.index(ligne), ligne.index(case), "placement") == True or self.flip_vertical(self.lesCases, couleur, self.lesCases.index(ligne), ligne.index(case), "placement") == True or self.flip_diagonal(self.lesCases, couleur, self.lesCases.index(ligne), ligne.index(case), "placement") == True:
                            if self.check_autour(ligne, case) == True:
                                self.can.create_oval(case[0][0] + 2,case[1][0] + 2,case[0][1] - 2, case[1][1] - 2, fill=couleur, outline=couleur)
                                self.move_counter += 1
                                self.lesCases[self.lesCases.index(ligne)][ligne.index(case)] = [(case[0][0], case[0][1]), (case[1][0], case[1][1]), True, couleur]
                                case = [(case[0][0], case[0][1]), (case[1][0], case[1][1]), True, couleur]
                                self.flip_horizontal(self.lesCases, couleur, self.lesCases.index(ligne), ligne.index(case), "nonplacement")
                                self.flip_vertical(self.lesCases, couleur, self.lesCases.index(ligne), ligne.index(case), "nonplacement")
                                self.flip_diagonal(self.lesCases, couleur, self.lesCases.index(ligne), ligne.index(case), "nonplacement")
                            else:
                                showerror("Erreur", "Vous ne pouvez pas placer un pion ici, il doit y avoir au moins 1 pion sur une case adjacente.")

                        elif self.move_counter == (self.grille_size ** 2 - 4) and self.flip_horizontal(self.lesCases, couleur, self.lesCases.index(ligne), ligne.index(case), "placement") == False or self.flip_vertical(self.lesCases, couleur, self.lesCases.index(ligne), ligne.index(case), "placement") == False or self.flip_diagonal(self.lesCases, couleur, self.lesCases.index(ligne), ligne.index(case), "placement") == False:
                            self.game_over()
                    
                        else:
                            showerror("Erreur", "Vous devez obligatoirement pouvoir retourner un pion.")
                            
                    elif ((case[0][0] < x < case[0][1]) and (case[1][0] < y < case[1][1])) and (case[2] == True):
                        showerror("Erreur", "Vous ne pouvez pas joueur sur un pion existant.")
                    
                except:
                    pass

            for ligne in self.lesCases:
                for case in ligne:
                    if isinstance(case, list) == True:
                        if case[2] == True:
                            self.can.create_oval(case[0][0] + 2,case[1][0] + 2,case[0][1] - 2, case[1][1] - 2, fill=case[3], outline=case[3])
        
        self.p1_var_int = IntVar(value=0)
        self.p2_var_int = IntVar(value=0)
        for ligne in self.lesCases:
            for case in ligne:
                if isinstance(case, list) == True:
                    if case[3] == 'snow':
                        self.p1_var_int = IntVar(value=self.p1_var_int.get() + 1)
                        self.p1_var_str.set(self.p1_var_int.get())
                    elif case[3] == 'gray24':
                        self.p2_var_int = IntVar(value=self.p2_var_int.get() + 1)
                        self.p2_var_str.set(self.p2_var_int.get())
        
        if (self.p1_var_int.get() + self.p2_var_int.get()) == (self.grille_size ** 2) : #when the board is filled up
            self.game_over()
            
    def game_over(self):
        if self.p1_var_int.get() > self.p2_var_int.get():
            self.winner.set(value='p1')
            showinfo("Victoire", "Congratulations Joueur 1 !\n Pour rejouer clicker 'Effacer' et ensuite 'Jouer'")
        elif self.p1_var_int.get() < self.p2_var_int.get():
            self.winner.set(value='p2')
            showinfo("Victoire", "Congratulations Joueur 2 !\n Pour rejouer clicker 'Effacer' et ensuite 'Jouer'")
        else:
            self.winner.set(value='draw')
            showinfo("Egalité !", "Egalité !\n Pour rejouer clicker 'Effacer' et ensuite 'Jouer'")
            

    def affiche(self):
        for element in self.lesCases:
            for truc in element:
                print(truc)
            print()


    def clear(self):
        "Nettoyage du canevas"
        self.can.delete("all")
        self.lesCases.clear()
        self.p1_var_int.set(value=2)
        self.p2_var_int.set(value=2)

