from tkinter import *


def apresentar():
    print(valor_check.get())

menu_inicial = Tk()
menu_inicial.title('CheckButton')

valor_check = IntVar()

check = Checkbutton(menu_inicial,
                    text='Esta é uma checkbox',
                    variable=valor_check,
                    command=apresentar).grid()

menu_inicial.mainloop()
