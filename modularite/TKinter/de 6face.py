from tkinter import *
from math import *
from random import *

# Création de la fenêtre principale
Mafenetre=Tk()


textNombre = StringVar(Mafenetre, "")
def LancerDes():
    print("des lancé")
    r = round(random()*6)
    textNombre.set(str(r))
# Création d'un widget Label
Text = Label(Mafenetre, textvariable = textNombre, fg = 'red')


# Création d'un widget Button
BoutonQuitter = Button(Mafenetre, text = 'Quitter', command = Mafenetre.destroy)


BoutonLancer = Button(Mafenetre, text = 'Lancer', command = LancerDes)
BoutonLancer.pack(side=LEFT, padx =3, pady =3)
BoutonQuitter.pack(side=LEFT, padx =3, pady =3)
Text.pack(side=RIGHT, padx =3, pady =3)

# Lancement de la boucle infinie (gestionnaire d'événements)
Mafenetre.mainloop() 