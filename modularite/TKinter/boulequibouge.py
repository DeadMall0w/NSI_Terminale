from tkinter import *
from math import *
from random import *
from time import *
# Création de la fenêtre principale
fen=Tk()


can=Canvas(fen,width=1000,height=1000,background='black') 
can.focus_set() 

speed = 5
boulePOs = (0,0)

def afficher():
    can.delete("all")
    can.create_oval(boulePOs[0],boulePOs[1],boulePOs[0]+100,boulePOs[1]+100,outline="black",fill="red")

def pos(position):
    global boulePOs

    boulePOs = (boulePOs[0] + position[0], boulePOs[1] + position[1])
    afficher()


def Up(event):
    pos((0,speed))

def Down(event):
    pos((0,-speed))

def Right(event):
    pos((speed,0))

def Left(event):
    pos((-speed,0))
    


def Quitter():
    exit()


can.bind("<KeyPress-z>",Down)
can.bind("<KeyPress-s>",Up)
can.bind("<KeyPress-q>",Left)
can.bind("<KeyPress-d>",Right)
    

    
    
    
# # Création d'un widget Label
# text = Label(fen, text = "Mot de passe")



# BoutonValider = Button(fen, text = 'Valider', command = Valider)


# BoutonValider.pack(side=RIGHT, padx =3, pady =3)
# text.pack(side=LEFT, padx =3, pady =3)
# inputtxt.pack(side=LEFT, padx =3, pady =3)






can.pack()
# Lancement de la boucle infinie (gestionnaire d'événements)
fen.mainloop() 


# for i in range(20):
#     Up()
#     sleep(1)

# #can.delete("all")