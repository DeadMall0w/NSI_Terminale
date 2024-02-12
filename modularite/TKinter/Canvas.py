from tkinter import *
from math import *
from random import *

# Création de la fenêtre principale
fen=Tk()

inputtxt = Entry(fen, show="*")

def Quitter():
    exit()

can=Canvas(fen,width=1000,height=1000,background='red') 
img = PhotoImage(file='astroneer-bongo.gif')
Label(
    fen,
    image=img
)
can.create_image(255,10,anchor="n",image=img)
    

    
    
    
# # Création d'un widget Label
# text = Label(fen, text = "Mot de passe")



# BoutonValider = Button(fen, text = 'Valider', command = Valider)


# BoutonValider.pack(side=RIGHT, padx =3, pady =3)
# text.pack(side=LEFT, padx =3, pady =3)
# inputtxt.pack(side=LEFT, padx =3, pady =3)






can.pack()
# Lancement de la boucle infinie (gestionnaire d'événements)
fen.mainloop() 