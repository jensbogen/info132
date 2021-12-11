#big018_t9

#Oppgave 1.)

from tkinter import Tk, Label, Button

rotvindu = Tk()

farvel = Label(rotvindu)

def lukk_vindu(): #Funksjon som lukker vinduet
    rotvindu.destroy()

knapp = Button(rotvindu, text="Farvel",
               command=lukk_vindu)

knapp.grid(row=1, column=1)

rotvindu.mainloop()

#Oppgave 2.)
from tkinter import Tk, Label, Button, StringVar
nummer = 0

def klikk(): #Funksjon som legger til 1 per klikk
    global nummer
    nummer += 1
    knapp.set(nummer)

vindu1 = Tk()
tittel1 = Label(vindu1, text="Trykk på knappen under!")
tittel1.pack()

knapp = StringVar()
knapp.set('0')

knapp1 = Button(vindu1, textvariable = knapp, command = klikk)
knapp1.pack()

vindu1.mainloop()
