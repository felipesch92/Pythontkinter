from tkinter import *


def mostrarNome():
    nome = txt_nome.get()
    if nome:
        label_final = Label(menu_inicial,
                            text=f'O teu nome é {nome}')
        label_final.grid()

# GUI
menu_inicial = Tk()
menu_inicial.title('Título')
menu_inicial.geometry('200x150')
menu_inicial.resizable(False, False)

# Criar os widgets
label_1 = Label(menu_inicial, text='O teu nome')
txt_nome = Entry(menu_inicial)
btn_executar = Button(menu_inicial, text='Executar', command=mostrarNome)
# Organizar os widgets
label_1.grid()
txt_nome.grid()
btn_executar.grid()

menu_inicial.mainloop()
