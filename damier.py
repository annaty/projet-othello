from math import *
# o --> bleu
# x --> rouge
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

class Damier():
    def __init__(self, canevas):
        self.can = canevas
        self.lesCases = []
        self.move_counter = 1

    def creation_grille(self, taille):
        grille = []
        y1 = 10
        y2 = y1 + 30
        for row in range(0, taille + 2):
            grille.append([])
            x1 = 10
            x2 = x1 + 30
            if row == 0: #premier ligne
                grille[row].append(" ")
                # self.can.create_rectangle(x1, y1, x2, y2, outline='gray64') # top left corner
                self.lesCases.append([(x1, x2),(y1, y2), False, ""])
                for column in range(1, taille + 2):
                    if column == taille + 1:
                        grille[row].append('_')
                        self.lesCases.append([(x1, x2),(y1, y2), False, ""])
                    else:
                        x1 += 30
                        x2 += 30
                        grille[row].append(column)
                        self.can.create_rectangle(x1, y1, x2, y2, outline='light steel blue')
                        self.can.create_text(x1+15, y1+15, text = column)
                        self.lesCases.append([(x1, x2),(y1, y2), False, ""])
            elif row == taille + 1: # derniere ligne
                grille[row].append(" ")
                self.lesCases.append([(x1, x2),(y1, y2), False, ""])
                for column in range(1, taille + 2):
                    if column == taille + 1: # derniere colonne
                        grille[row].append('_')
                        self.lesCases.append([(x1, x2),(y1, y2), False, ""])
                    else:
                        x1 += 30
                        x2 += 30
                        grille[row].append(column)
                        self.lesCases.append([(x1, x2),(y1, y2), False, ""])
            else: # autres lignes
                grille[row].append(row)
                self.can.create_rectangle(x1, y1, x2, y2, outline='light steel blue')
                self.can.create_text(x1 +15, y1 + 15, text = grille[row][0])
                self.lesCases.append([(x1, x2),(y1, y2), False, ""])
                x1 += 30
                x2 += 30
                for column in range(1, taille + 2):
                    if column == taille + 1:
                        self.lesCases.append([(x1, x2),(y1, y2), False, ""])
                        grille[row].append("_")
                    else:
                        grille[row].append(".")
                        self.can.create_rectangle(x1, y1, x2, y2, outline='gray50')
                        self.lesCases.append([(x1, x2),(y1, y2), False, ""])
                        x1 += 30
                        x2 += 30
                    
            y1 += 30
            y2 += 30
            
        #=============   position de depart   =======================
        milieu = int(floor(len(grille)*30-10) / 2)
        padd = 2
        
        self.can.create_oval(milieu + padd + 15, milieu + padd + 15, milieu + 28 + 15 , milieu + 28 + 15, fill='snow', outline='snow')
        self.lesCases.remove([(milieu + 15, milieu + 30 + 15),(milieu + 15, milieu + 30 + 15), False, ""])
        self.lesCases.append([(milieu + 15, milieu + 30 + 15),(milieu + 15, milieu + 30 + 15), True, "blue"])

        self.can.create_oval(milieu + padd - 15, milieu + padd - 15, milieu + 28 - 15 , milieu + 28 - 15, fill='snow', outline='snow')
        self.lesCases.remove([(milieu - 15, milieu + 30 - 15),(milieu - 15, milieu + 30 - 15), False, ""])
        self.lesCases.append([(milieu - 15, milieu + 30 - 15),(milieu - 15, milieu + 30 - 15), True, "blue"])

        self.can.create_oval(milieu + padd + 15,  milieu + padd - 15, milieu + 28 + 15 , milieu + 28 - 15, fill='gray24', outline='gray24')
        self.lesCases.remove([(milieu + 15, milieu + 30 + 15),(milieu - 15, milieu + 30 - 15), False, ""])
        self.lesCases.append([(milieu + 15, milieu + 30 + 15),(milieu - 15, milieu + 30 - 15), True, "red"])

        self.can.create_oval(milieu + padd - 15, milieu + padd + 15, milieu + 28 - 15 , milieu + 28 + 15, fill='gray24', outline='gray24')
        self.lesCases.remove([(milieu - 15, milieu + 30 - 15),(milieu + 15, milieu + 30 + 15), False, ""])
        self.lesCases.append([(milieu - 15, milieu + 30 - 15),(milieu + 15, milieu + 30 + 15), True, "red"])



    def check_autour(self, case_list, x1, x2, y1, y2):
        case_counter = 0
        for case in self.lesCases:
            if case[0] == (x1 + 30, x2 + 30) and case[1] == (y1, y2):       # Case DROITE
                if not case[2] :
                    case_counter += 1
            if case[0] == (x1 - 30, x2 - 30) and case[1] == (y1, y2):        # Case GAUCHE
                if not case[2] :
                    case_counter += 1
            if case[0] == (x1, x2) and case[1] == (y1 + 30, y2 + 30):        # Case HAUT
                if not case[2] :
                    case_counter += 1
            if case[0] == (x1, x2) and case[1] == (y1 - 30, y2 - 30):        # Case BAS 
                if not case[2] :
                    case_counter += 1
            if case[0] == (x1 + 30, x2 + 30) and case[1] == (y1 - 30 , y2 - 30):        # Case diag DROITE HAUT
                if not case[2] :
                    case_counter += 1
            if case[0] == (x1 + 30, x2 + 30) and case[1] == (y1 + 30, y2 + 30):        # Case diag DROITE BAS
                if not case[2] :
                    case_counter += 1
            if case[0] == (x1 - 30, x2 - 30) and case[1] == (y1 + 30, y2 + 30):        # Case diag GAUCHE HAUT
                if not case[2] :
                    case_counter += 1
            if case[0] == (x1 - 30, x2 - 30) and case[1] == (y1 - 30, y2 - 30):        # Case diag GAUCHE BAS
                if not case[2] :
                    case_counter += 1
                
        return not case_counter == 8


    def posePion(self, event):
        x = event.x
        y = event.y

        if self.move_counter % 2 == 0:
            couleur = 'gray24'
        elif self.move_counter % 2 == 1:
            couleur = 'snow'

        for case in self.lesCases:
            if ((case[0][0] < x < case[0][1]) and (case[1][0] < y < case[1][1])) and (case[2] == False):
                if self.check_autour(self.lesCases, case[0][0], case[0][1], case[1][0], case[1][1]) == True:
                    self.can.create_oval(case[0][0] + 2,case[1][0] + 2,case[0][1] - 2,case[1][1] - 2,fill=couleur, outline=couleur)
                    case_index = self.lesCases.index(case)
                    self.lesCases[case_index][2] = True
                    self.move_counter += 1
                else:
                    error = Toplevel()  # Popup -> Toplevel()
                    error.title('Infos')
                    canerror = Canvas(error, bg='white', height=200, width=200)
                    canerror.pack(side=LEFT)
                    Button(error, text='Quitter', command=error.destroy).pack(padx=10, pady=10)
                    mytext = canerror.create_text(100, 100, text="Il n'y a rien autour, veuillez choisir un autre champs")
                    mytext.pack()
            elif ((case[0][0] < x < case[0][1]) and (case[1][0] < y < case[1][1])) and (case[2] == True):
                error = Toplevel()  # Popup -> Toplevel()
                error.title('Infos')
                canerror = Canvas(error, bg='white', height=200, width=200)
                canerror.pack(side=LEFT)
                Button(error, text='Quitter', command=error.destroy).pack(padx=10, pady=10)
                mytext = canerror.create_text(100, 100, text="Ce champs est deja pris")
                mytext.pack()


    def clear(self):
        "Nettoyage du canevas"
        self.can.delete("all")
        self.lesCases.clear()