from damier import Damier
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

def game_window(size):
    # Création du widget principal ("maître") :
    fen1 = Tk()
    fen1.title('Othello')
    # fen1.iconphoto(True, PhotoImage(file='icon.png'))
    # Création des widgets "esclaves" :
    can1 = Canvas(fen1, bg='light steel blue', height=70+size*30, width=70+size*30)
    can1.pack(anchor='center')

    # Creation du damier
    d = Damier(can1)
    bou1 = Button(fen1, text='Quitter', command=fen1.quit)
    bou1.pack(side=BOTTOM)

    can1.bind("<Button-1>", d.posePion)  # on rajoute un evenement "pointeur" quand on clique gauche
    bou2 = Button(fen1, text='Jouer', command= lambda : d.creation_grille(size))
    bou2.pack(side=TOP)
    bou3 = Button(fen1, text='Effacer', command=d.clear)
    bou3.pack()

    #points
    p1 = d.p1_var_str
    p2 = d.p2_var_str
    p1_color = Label(fen1, anchor=CENTER, text='White: ')
    points1 = Label(fen1, anchor=CENTER, textvariable=p1)
    p2_color = Label(fen1, anchor=CENTER, text='Black: ')
    points2 = Label(fen1, anchor=CENTER, textvariable=p2)

    # l1.insert(INSERT, p1)
    p1_color.pack(side='left')
    points1.pack(side='left')
    p2_color.pack(side='left')
    points2.pack(side='left')

    fen1.mainloop()  # démarrage du réceptionnaire d'événement
    fen1.destroy()  # destruction (fermeture) de la fenêtre
    
def board_size():
    try:
        size_input = int(input_box.get())
        if 20 >= size_input >= 4 and size_input % 2 == 0:
            fen0.destroy()
            game_window(size_input)
        else:
            input_error.config(text="Votre valeur n'est pas valide, entre en une autre.")
    except:
        input_error.config(text="Veuillez entrer un nombre entier...")

fen0 = Tk()
fen0.title('Size input')

input_label = Label(fen0, text=" Quelle taille de plateau voulez-vous ? Entrez une valeur paire, d'au moins 4 : ")
input_label.pack(pady=20)

input_box = Entry(fen0)
input_box.pack(pady=10)

input_submit = Button(fen0, text="Submit size", command=board_size)
input_submit.pack()
# fen0.bind('<Return>', board_size)

input_error = Label(fen0, text='')
input_error.pack(pady=20)

fen0.mainloop()