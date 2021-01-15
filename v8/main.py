from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Título')
menu_inicial.geometry('500x300')
menu_inicial.resizable(False, False)

label1 = Label(
    menu_inicial,
    text='Frase de testes',
    font='Arial 20',
    bd=1,
    relief='solid',
    width=25,
    height=2
).pack()

menu_inicial.mainloop()