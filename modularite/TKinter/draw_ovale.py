from tkinter import *
from math import *
from random import *

# Création de la fenêtre principale
fen=Tk()


can=Canvas(fen,width=1000,height=1000,background='black') 
can.focus_set() 


# def clavier(event):  
#     can.create_oval(event.x,event.y,event.x+50,event.y+50,outline="black",fill="red")
#     print("souris pressée")
mousePos = (0,0)
deja_clique = 0
startPos = (0,0)
endPos = (0,0)

def afficher():
    can.delete("all")
    can.create_oval(startPos[0],startPos[1],endPos[0],endPos[1],outline="black",fill="red")

def mouse(event):
    global mousePos
    global endPos
    global startPos
    global deja_clique 

    mousePos = (event.x, event.y)
    if deja_clique == 1:
        endPos = mousePos
        afficher()
    


def click(event):
    global mousePos
    global endPos
    global startPos
    global deja_clique 

    if deja_clique == 0:
        startPos = mousePos
        deja_clique = 1
    elif deja_clique == 1:
        endPos = mousePos
        deja_clique = 2


def Quitter():
    exit()


can.bind("<Motion>",mouse)
can.bind("<Button-1>", click)

    

    
    
    
# # Création d'un widget Label
# text = Label(fen, text = "Mot de passe")



# BoutonValider = Button(fen, text = 'Valider', command = Valider)


# BoutonValider.pack(side=RIGHT, padx =3, pady =3)
# text.pack(side=LEFT, padx =3, pady =3)
# inputtxt.pack(side=LEFT, padx =3, pady =3)






can.pack()
# Lancement de la boucle infinie (gestionnaire d'événements)
fen.mainloop() 


#can.delete("all")