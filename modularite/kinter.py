from tkinter import *
from random import *
from math import *
 
Main_window = Tk()
 
my_text = str(round(random()*6))
 
def counter():
    global my_text
     
    my_text = str(round(random()*6))
    my_label.config(text = my_text)
 
my_button = Button(Main_window,
                   text = "Generer",
                   command = counter)

my_label = Label(Main_window,
                 text = "")
 
my_label.pack(side=RIGHT,padx = 3,pady = 3)
my_button.pack(side=LEFT,padx = 3,pady = 3)


Main_window.mainloop()