from tkinter import *
from math import *
from random import *

# Création de la fenêtre principale
fen=Tk()


can=Canvas(fen,width=1000,height=1000,background='black') 
can.focus_set() 


def clavier(event):  
    can.create_oval(event.x,event.y,event.x+50,event.y+50,outline="black",fill="red")
    print("souris pressée")

def Quitter():
    exit()


can.bind("<B1-Motion>",clavier)

    

    
    
    
# # Création d'un widget Label
# text = Label(fen, text = "Mot de passe")



# BoutonValider = Button(fen, text = 'Valider', command = Valider)


# BoutonValider.pack(side=RIGHT, padx =3, pady =3)
# text.pack(side=LEFT, padx =3, pady =3)
# inputtxt.pack(side=LEFT, padx =3, pady =3)






can.pack()
# Lancement de la boucle infinie (gestionnaire d'événements)
fen.mainloop() 