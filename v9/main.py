from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Título')
menu_inicial.geometry('500x300')

label1 = Label(
    menu_inicial,
    text='Frase 1',
    font='Arial 20',
    bd=1,
    relief='solid',
    width=30,
    height=5,
    anchor=W
)
label1.pack()

menu_inicial.mainloop()
