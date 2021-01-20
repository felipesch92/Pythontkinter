from tkinter import *


# Funções
def mostrar_nome():
    vartexto.set(textbox1.get())


# GUI
menu_inicial = Tk()
menu_inicial.title('Aplicativo')
vartexto = StringVar()

# widgets
label1 = Label(menu_inicial,
               text='O teu nome é: ')
textbox1 = Entry(menu_inicial)
botao1 = Button(menu_inicial,
                text='Executar', command=mostrar_nome)
label2 = Label(menu_inicial, textvariable=vartexto)
label3 = Label(menu_inicial, textvariable=vartexto)
label4 = Label(menu_inicial, textvariable=vartexto)

# layout
label1.grid()
textbox1.grid()
botao1.grid()
label2.grid()
label3.grid()
label4.grid()

# Widgets

menu_inicial.mainloop()