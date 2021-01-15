from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Título')
menu_inicial.geometry('500x300')

texto = StringVar()
texto.set('Novo texto')

label1 = Label(
    menu_inicial,
    textvariable=texto,
    font='Arial 20',
    bg='red',
    fg='white'
)
label1.pack()

label2 = Label(
    menu_inicial,
    textvariable=texto,
    font='Arial 20',
    bg='green',
    fg='white'
)
label2.pack()

texto.set('Felipe Schmaedecke')

menu_inicial.mainloop()
