from tkinter import *
menu_inicial = Tk()
menu_inicial.title('Primeira tela')

#Define o tamanho e a posição do formulário na tela
menu_inicial.geometry('500x250+300+200')
#Define se a altura e largura serão redimensionáveis
menu_inicial.resizable(False, False)

#Define até que tamanho o usuário pode aumentar ou diminuir o formulário
#menu_inicial.minsize(width=500, height=250)
#menu_inicial.maxsize(width=700, height=400)



menu_inicial.mainloop()
