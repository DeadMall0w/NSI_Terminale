from tkinter import *
from math import *
from random import *

# Création de la fenêtre principale
Mafenetre=Tk()

inputtxt = Entry(Mafenetre, show="*")

def Quitter():
    exit()

def CBon():
    popup = Tk()
    popup.wm_title("Resultat")
    okTXT = Label(popup, text = "Mot de passe correcte, Au revoir !")
    okBTN = Button(popup, text = "OK", command = Quitter)
    okTXT.pack()
    okBTN.pack()
    
    
def CPASBon():
    popup = Tk()
    popup.wm_title("Resultat")
    okTXT = Label(popup, text = "Mot de passe incorrecte, Reéssayez !")
    okBTN = Button(popup, text = "OK", command = popup.destroy)
    okTXT.pack()
    okBTN.pack()
    
def Valider():
    if inputtxt.get() == "RafEstLeMeilleur":
        CBon()
    else:
        CPASBon()
    
    

    
    
    
# Création d'un widget Label
text = Label(Mafenetre, text = "Mot de passe")



BoutonValider = Button(Mafenetre, text = 'Valider', command = Valider)


BoutonValider.pack(side=RIGHT, padx =3, pady =3)
text.pack(side=LEFT, padx =3, pady =3)
inputtxt.pack(side=LEFT, padx =3, pady =3)







# Lancement de la boucle infinie (gestionnaire d'événements)
Mafenetre.mainloop() 