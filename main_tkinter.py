from damier import Damier
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

def start_game():
    fen0 = Tk()
    fen0.title('Size input')

    input_label = Label(fen0, text=" Quelle taille de plateau voulez-vous ? Entrez une valeur paire, d'au moins 4 : ")
    input_label.pack(pady=20)

    input_box = Entry(fen0)
    input_box.pack(pady=10, padx=10)

    input_submit = Button(fen0, text="Submit size", command= lambda : board_size(fen0, input_box, input_error))
    input_submit.pack()
    # fen0.bind('<Return>', board_size)

    input_error = Label(fen0, text='')
    input_error.pack(pady=10, padx=10)

    fen0.mainloop()

def board_size(master_window, size, error):
    try:
        size_input = int(size.get())
        if 20 >= size_input >= 4 and size_input % 2 == 0:
            master_window.destroy()
            game_window(size_input)
        else:
            error.config(text="Votre valeur n'est pas valide, entre en une autre.")
    except:
        error.config(text="Veuillez entrer un nombre entier...")

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
    
    #points
    p1 = d.p1_var_str
    p2 = d.p2_var_str
    
    p1_color = Label(fen1, anchor=CENTER, text='White: ')
    points1 = Label(fen1, anchor=CENTER, textvariable=p1)
    p2_color = Label(fen1, anchor=CENTER, text='Black: ')
    points2 = Label(fen1, anchor=CENTER, textvariable=p2)
    p1_color.pack(side='left')
    points1.pack(side='left')
    p2_color.pack(side='left')
    points2.pack(side='left')

    #buttons
    bou1 = Button(fen1, text='Quitter', command=fen1.quit)
    bou1.pack(side='bottom')
    can1.bind("<Button-1>", d.posePion)  # on rajoute un evenement "pointeur" quand on clique gauche
    bou3 = Button(fen1, text='Effacer', command=d.clear)
    bou3.pack(side='bottom')
    bou2 = Button(fen1, text='Jouer', command= lambda : d.creation_grille(size))
    bou2.pack(side='bottom')

    #endgame condition
    my_state = d.fullboard_state
    my_state.trace_add('read', end_game(fen1, d))

    fen1.mainloop()  # démarrage du réceptionnaire d'événement
    fen1.destroy()  # destruction (fermeture) de la fenêtre

def end_game(master_window, board_instance):
    print('is the board full :', board_instance.board_state)
    if board_instance.winner != '':
        print('we got in')
        master_window.destroy()
        fen2 = Tk()
        fen2.title('Othello - Game Over')

        if board_instance.p1_var_int.get() > board_instance.p2_var_int.get(): #if player1 wins
            Label(fen2, anchor=CENTER, text="Joueur 1 a gagne").pack()
        elif board_instance.p1_var_int.get() < board_instance.p2_var_int.get(): #if player2 wins
            Label(fen2, anchor=CENTER, text="Joueur 2 a gagne").pack()
        else: #draw
            Label(fen2, anchor=CENTER, text="Un match nul").pack()

        Label(fen2, anchor=CENTER, text="Merci d'avoir joue").pack()
        b_replay = Button(fen2, text='Rejouer', command= start_game)
        b_replay.pack(side='bottom')

        fen2.mainloop()  # démarrage du réceptionnaire d'événement
        fen2.destroy()  # destruction (fermeture) de la fenêtre
    else:
        print('else works')


start_game()