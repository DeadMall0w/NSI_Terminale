from tkinter import *
from random import *
from math import *
 
Main_window = Tk()
Main_window.geometry("600x200")
 
my_text = str(round(random()*6))
 
 
def display_text():
    global entry
    string= entry.get()
    label.configure(text=string)
   
label=Label(Main_window, text="", font=("Courier 22 bold"))


#Create an Entry widget to accept User Input
entry= Entry(Main_window, width= 40)
entry.focus_set()
entry.pack()

def counter():
    global my_text
     
    my_text = str(round(random()*6))
    my_label.config(text = my_text)
 
my_button = Button(Main_window,
                   text = "Valider",
                   command = counter)

my_label = Label(Main_window,
                 text = "Entrez le mot de passe sinon la mort vous attend : ")
 
my_label.pack(side=LEFT,padx = 3,pady = 3)
label.pack(side=LEFT,padx = 3,pady = 3)
my_button.pack(side=RIGHT,padx = 3,pady = 3)


Main_window.mainloop()