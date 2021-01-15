from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Formulário')

menu_inicial.geometry('500x300+100+100')
menu_inicial.resizable(False, False)


def mostra(mensagem):
    print(mensagem)


# Botão
btn = Button(menu_inicial, text='Executar', command=lambda: mostra('Olá mundo!'))
btn.pack()

btn2 = Button(menu_inicial, text='Clicar', command=lambda: print('OK'))
btn2.pack()

menu_inicial.mainloop()
