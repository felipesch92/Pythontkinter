from tkinter import *


def mostrar():
    lb1['text'] = 'Texto alterado.'

menu_inicial = Tk()
menu_inicial.title('Executável')

lb1 = Label(menu_inicial)
btn_executar = Button(menu_inicial,
                      text='Executar',
                      command=mostrar)
lb1.grid(row=0, column=0)
btn_executar.grid(row=1, column=0)

menu_inicial.mainloop()
