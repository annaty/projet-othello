from damier import Damier
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import webbrowser

#Gestion des erreurs quand on rentre la taille de la grille
def board_size(master_window, size, error):
    try:
        size_input = int(size.get())
        if 20 >= size_input >= 4 and size_input % 2 == 0:
            master_window.destroy()
            game_window(size_input)
        else:
            error.config(text="Votre valeur n'est pas valide, entrez en une autre.")
    except:
        error.config(text="Veuillez entrer un nombre entier...")


# Lancement du jeu
def game_window(size):
    
    # Création du widget principal ("maître") :
    fen1 = Tk()
    fen1.title('Othello')
    fen1.iconbitmap('icon3.ico')

    # Création des widgets "esclaves" :
    can1 = Canvas(fen1, bg='light steel blue', height=70+size*30, width=70+size*30)
    can1.pack(anchor='center')

    # Creation du damier
    d = Damier(can1)
    
    #points
    p1 = d.p1_var_str
    p2 = d.p2_var_str
    
    #Affichage des joueurs, points sur la grille
    p1_color = Label(fen1, anchor='w', text='Blanc: ')
    points1 = Label(fen1, anchor='w', textvariable=p1)
    p2_color = Label(fen1, anchor='w', text='Noir: ')
    points2 = Label(fen1, anchor='w', textvariable=p2)
    p1_color.pack()
    points1.pack()
    p2_color.pack()
    points2.pack()

    current_player = d.current_player
    turn_label = Label(fen1, anchor='w', text='le tour est au: ')
    turn_player = Label(fen1, anchor='w', textvariable=current_player)
    turn_label.pack()
    turn_player.pack()

    #buttons
    bou1 = Button(fen1, text='Quitter', command=fen1.quit)
    bou1.pack(side='right')
    can1.bind("<Button-1>", d.posePion)  # on rajoute un evenement "pointeur" quand on clique gauche
    bou3 = Button(fen1, text='Effacer', command=d.clear)
    bou3.pack(side='right')
    bou2 = Button(fen1, text='Jouer', command= lambda : d.creation_grille(size))
    bou2.pack(side='right')
    d.countpass = 0

    # Fonction permettant de passer son tour
    def skip_turn(): 
        d.move_counter +=1
        d.countpass += 1
        if d.countpass == 2: # Si le tour est passé de fois (par les deux joueurs), la partie se termine
            d.game_over()
        else:
            if d.current_color == 'snow':
                d.current_player.set(value='Noir')
            elif d.current_color == 'gray24':
                d.current_player.set(value='Blanc')
            else:
                pass

    bou4 = Button(fen1, text='Passer son tour', command=skip_turn) 
    bou4.pack(side='bottom')

    fen1.mainloop()  # démarrage du réceptionnaire d'événement
    fen1.destroy()  # destruction (fermeture) de la fenêtre

def callback(url):
    webbrowser.open_new(url)

fen0 = Tk()
fen0.title('Othello - saisie de la taille')
fen0.iconbitmap('icon3.ico')

welcome = Label(fen0, text=" Bienvenue ! Pour lire les règles du jeu clickez sur le bouton ci-dessous, il va ouvrir un lien dans votre navigateur.")
welcome.pack(pady=10, padx=20)

# Bouton "Règles"
link = Label(fen0, text="Règles",borderwidth=3, relief='solid',font=('arial', 18), cursor="hand2")
link.bind("<Button-1>", lambda e: callback("https://www.ffothello.org/othello/regles-du-jeu/"))
link.pack(pady=10, padx=10)

# Entrée pour la taille du plateau
input_label = Label(fen0, text=" Quelle taille de plateau voulez-vous ? Entrez une valeur paire, d'au moins 4 : ")
input_label.pack()

input_box = Entry(fen0)
input_box.pack(pady=5,padx=10)

input_submit = Button(fen0, text="Entrer", command= lambda : board_size(fen0, input_box, input_error))
input_submit.pack()

# Affichage des erreurs
input_error = Label(fen0, text='')
input_error.pack(pady=10, padx=10)

fen0.mainloop()
