from math import *
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
class Damier():
    def __init__(self, canevas):
        self.can = canevas
        self.lesCases = [] # La liste qui va comporter toutes les cases avec leurs attributs
        self.move_counter = 1
        self.current_color = ''
        self.countpass = 0

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
        self.current_player = StringVar(value='')

    # Fonction qui construit la grille, elle est appelée quand on clique sur "Jouer"
    def creation_grille(self, taille):
        self.current_player.set(value='Blanc')
        self.move_counter = 1
        self.grille_size = taille
        grille = []
        y1 = 10
        y2 = y1 + 30
        for ligne in range(0, taille + 2):
            x1 = 10
            x2 = x1 + 30
            self.lesCases.append([])
            if ligne == taille + 1:
            # C'est la toute dernière ligne, elle n'apparait pas dans la fenetre, elle sert de limite
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
                        # C'est la toute dernière colonne, elle n'apparait pas dans la fenetre, elle sert de limite
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
            self.p1_var_int.set(2)
            self.p1_var_str.set(2)
            self.p2_var_int.set(2)
            self.p2_var_str.set(2)
            
        #=============   positions de depart   =======================
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

        # On initialise donc le core de chaque joueur à 2 du fait des pions de départ
        self.p1_var_int = IntVar(value=2)
        self.p2_var_int = IntVar(value=2)

    # Fonction qui vérifié si le pion posé est entourré ou non
    def check_autour(self, laLigne, laCase):
        # laLigne et laCase correspondent à l'emplacement du pion posé dans la liste lesCases
        case_counter = 0
        try :
            if self.lesCases[self.lesCases.index(laLigne)][laLigne.index(laCase) + 1][2] == False:       # Case DROITE
                case_counter += 1
        except: # dans le cas où l'on est sur un bord, le try plus haut ne peut pas se faire, on passe alors dans le except
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
        # S'il n'y a rien autour du pion posé, la fonction retourne False
        # Dans le cas inverse, c'est True


    def check_valid_position(self, x, y):
        return (40 < x < (40 + 30 * 8) and 40 < y < (40 + 30 * 8))
    
    # Assigne se couleur au joueur et à son adversaire
    def color_assignment(self, pion_joue):
        if pion_joue == "snow": #Joueur 1
            return 'snow', 'gray24'
        elif pion_joue == "gray24": #Joueur 2
            return 'gray24', 'snow'
    
    #On fait appel à cette fonction dans tous les flips, elle vérifie si on a atteint la limite et ainsi retourner les pions
    def reached_limit(self, liste_champs, length_matrix):
        if "|" in liste_champs or "_" in liste_champs or " " in liste_champs:
            return True
        length_index_list = [index for index in range(1, length_matrix - 1)]
        for element in length_index_list:
            if element in liste_champs:
                return True
        return False


    # Toutes les fonctions flip fonctionnent de la même manière, c'est juste le sens de vérification qui change
    def flip_horizontal(self, grille, player, row, column, placement):
        #on mentionne la position du piont que l'on vient de poser
        player_piece, enemy_piece = self.color_assignment(player)
        check_list = [] # une liste qui contient le contenu de toutes les cellules dans la direction donnée
        i = 0 # une variable utilisée pour suivre le nombre d'itérations de la boucle

        #Eastern check
        try:
            # tant que notre limite n'est pas atteinte, on rentre dans cette boucle
            while self.reached_limit(check_list, len(grille)) == False:
                i+= 1
                east_cell_content = grille[row][column + i][3] # la couleur du pion de droite, la distance avec le pion posé dépend donc de i
                check_list.append(east_cell_content)
                if east_cell_content == player_piece and (enemy_piece in check_list) and check_list[0] != player_piece:
                    # east_cell_content == player_piece est notre limite, c'est lorsqu'on atteint un autre de ses pions, on peut alors retourner
                    for index_transform in range(1, i):
                        if placement == "placement": # Nous sert lorsque que l'on peut savoir s'il est posible de poser un pion ou non
                            # On utilise la fonction flip_horizontal pour la verification mais nous ne voulons pas retourner de pions
                            return True
                        else:
                            grille[row][column + index_transform][3] = player_piece
                    check_list[-1] = " "
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
                if west_cell_content == player_piece and (enemy_piece in check_list) and check_list[0] != player_piece:
                    for index_transform in range(1, i):
                        if placement == "placement":
                            return True
                        else:
                            grille[row][column - index_transform][3] = player_piece
                    check_list[-1] = " "
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
                if south_cell_content == player_piece and (enemy_piece in check_list) and check_list[0] != player_piece:
                    for index_transform in range(1, i):
                        if placement == "placement":
                            return True
                        else:
                            grille[row + index_transform][column][3] = player_piece
                    check_list[-1] = " "
        except:
            pass
        check_list.clear()
        i = 0

        #Northern check
        try:
            while self.reached_limit(check_list, len(grille)) == False:
                i+= 1
                north_cell_content = grille[row - i][column][3]
                check_list.append(north_cell_content)
                if north_cell_content == player_piece and (enemy_piece in check_list) and check_list[0] != player_piece:
                    for index_transform in range(1, i):
                        if placement == "placement":
                            return True
                        else:
                            grille[row - index_transform][column][3] = player_piece
                    check_list[-1] = " "
        except:
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
                if nw_cell_content == player_piece and (enemy_piece in check_list) and check_list[0] != player_piece:
                    for index_transform in range (1, i):
                        if placement == "placement":
                            return True
                        else:
                            grille[row - index_transform][column - index_transform][3] = player_piece
                    check_list[-1] = " "
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
                if se_cell_content == player_piece and (enemy_piece in check_list) and check_list[0] != player_piece:
                    for index_transform in range(1, i):
                        if placement == "placement":
                            return True
                        else:
                            grille[row + index_transform][column + index_transform][3] = player_piece
                    check_list[-1] = " "
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
                if sw_cell_content== player_piece and (enemy_piece in check_list) and check_list[0] != player_piece:
                    for index_transform in range(1, i):
                        if placement == "placement":
                            return True
                        else:
                            grille[row + index_transform][column - index_transform][3] = player_piece
                    check_list[-1] = " "
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
                if ne_cell_content == player_piece and (enemy_piece in check_list) and check_list[0] != player_piece:
                    for index_transform in range(1, i):
                        if placement == "placement":
                            return True
                        else:
                            grille[row - index_transform][column + index_transform][3] = player_piece
                    check_list[-1] = " "
        except:
            pass

    def posePion(self, event):
        x = event.x
        y = event.y

        # A chaque fois qu'on pose un pion on va devoir parcourir toutes les cases du plateau
        for ligne in self.lesCases:
            for case in ligne:
                # On définit la couleur du joueur
                if self.move_counter % 2 == 0:
                    self.current_color = 'gray24'
                    self.current_player.set(value='Noir')
                elif self.move_counter % 2 == 1:
                    self.current_color = 'snow'    
                    self.current_player.set(value='Blanc')
                try:
                    if ((case[0][0] < x < case[0][1]) and (case[1][0] < y < case[1][1])) and (case[2] == False):
                        
                        
                        # si il y a bien quelque chose autour du pion que l'on pose
                        if self.check_autour(ligne, case) == True:
                            # si le placement est bon (retourne obligatoirement un pion)
                            if self.flip_horizontal(self.lesCases, self.current_color, self.lesCases.index(ligne), ligne.index(case), "placement") == True or self.flip_vertical(self.lesCases, self.current_color, self.lesCases.index(ligne), ligne.index(case), "placement") == True or self.flip_diagonal(self.lesCases, self.current_color, self.lesCases.index(ligne), ligne.index(case), "placement") == True:

                                # A part la pose du pion, aucune modification n'est faite sur l'interface, la donnée se change uniquement dans la liste lesCases
                                self.countpass = 0
                                self.can.create_oval(case[0][0] + 2,case[1][0] + 2,case[0][1] - 2, case[1][1] - 2, fill=self.current_color, outline=self.current_color)
                                self.move_counter += 1
                                self.lesCases[self.lesCases.index(ligne)][ligne.index(case)] = [(case[0][0], case[0][1]), (case[1][0], case[1][1]), True, self.current_color]
                                case = [(case[0][0], case[0][1]), (case[1][0], case[1][1]), True, self.current_color]
                                self.flip_horizontal(self.lesCases, self.current_color, self.lesCases.index(ligne), ligne.index(case), "nonplacement")
                                self.flip_vertical(self.lesCases, self.current_color, self.lesCases.index(ligne), ligne.index(case), "nonplacement")
                                self.flip_diagonal(self.lesCases, self.current_color, self.lesCases.index(ligne), ligne.index(case), "nonplacement")
                            
                            else: # Sinon on retourne des messages d'erreur
                                showerror("Erreur", "Vous devez obligatoirement pouvoir retourner un pion.")
                        
                        else:
                            showerror("Erreur", "Vous ne pouvez pas placer un pion ici, il doit y avoir au moins 1 pion sur une case adjacente.")

                            
                    elif ((case[0][0] < x < case[0][1]) and (case[1][0] < y < case[1][1])) and (case[2] == True):
                        showerror("Erreur", "Vous ne pouvez pas jouer sur un pion existant.")
                    
                except:
                    pass
            
        # On examine les données que l'on a à présent dans lesCases et on modifie l'interface en fonction
        self.p1_var_int = IntVar(value=0)
        self.p2_var_int = IntVar(value=0)
        for ligne in self.lesCases:
            for case in ligne:
                if isinstance(case, list) == True:
                    if case[2] == True:
                        self.can.create_oval(case[0][0] + 2,case[1][0] + 2,case[0][1] - 2, case[1][1] - 2, fill=case[3], outline=case[3])
                    if case[3] == 'snow':
                        self.p1_var_int = IntVar(value=self.p1_var_int.get() + 1)
                        self.p1_var_str.set(self.p1_var_int.get())
                    elif case[3] == 'gray24':
                        self.p2_var_int = IntVar(value=self.p2_var_int.get() + 1)
                        self.p2_var_str.set(self.p2_var_int.get())

        # Si la grille est pleine, on affiche le gagnant
        if (self.p1_var_int.get() + self.p2_var_int.get()) == (self.grille_size ** 2) :
            self.game_over()
            
    # Fonction qui affiche le gagnant        
    def game_over(self):
        if self.p1_var_int.get() > self.p2_var_int.get():
            self.winner.set(value='p1')
            showinfo("Victoire", "Félicitations Joueur 1 !\n\nPour rejouer clicker 'Effacer' et ensuite 'Jouer'")
        elif self.p1_var_int.get() < self.p2_var_int.get():
            self.winner.set(value='p2')
            showinfo("Victoire", "Félicitations Joueur 2 !\n\nPour rejouer clicker 'Effacer' et ensuite 'Jouer'")
        else:
            self.winner.set(value='draw')
            showinfo("Egalité !", "Egalité !\n Pour rejouer clickez 'Effacer' et ensuite 'Jouer'")
            
    # Lorsque l'on clique sur "Effacer", nous effaçons tout le canevas et raprtons de zéro
    # C'est cette fonction qui efface tout
    def clear(self):
        "Nettoyage du canevas"
        self.can.delete("all")
        self.lesCases.clear()

