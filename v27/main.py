from tkinter import *


def executar():
    print(lista.get(ACTIVE))


menu_inicial = Tk()
menu_inicial.title('LISTBOX')

lista = Listbox(menu_inicial, selectmode=EXTENDED)
lista.grid()

# Inserir um item de cada vez
#lista.insert(0, 'Felipe')
#lista.insert(1, 'Tamara')
nomes = ['Felipe', 'Tamara', 'Dolores']
for n in nomes:
    lista.insert(END, n)

btn_clique = Button(menu_inicial,
                    text='Clique',
                    command=executar).grid()

menu_inicial.mainloop()
