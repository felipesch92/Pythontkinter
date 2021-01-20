from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Adicionar imagem a um layout')

img = PhotoImage(file='img/foto_fundo.png')

lbl_imagem = Label(menu_inicial,
                   image=img)
lbl_imagem.grid()
menu_inicial.mainloop()

#print(help(Label))