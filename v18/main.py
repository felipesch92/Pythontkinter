from tkinter import *


# Funções
# C - (F - 32) * 5/9
def calcular():
    f = float(textbox1.get())
    #c = f'{((f - 32) * 5/9):.2f}'
    c = (f - 32) * 5/9
    final.set(f'{round(c, 1)} graus Celsius')


# GUI
menu_inicial = Tk()
menu_inicial.title('Fahrenheit para Celsius')

final = StringVar()

# widgets
label1 = Label(menu_inicial,
               text='Graus Fahrenheit: ')
textbox1 = Entry(menu_inicial)
botao1 = Button(menu_inicial,
                text='Calcular', command=calcular)
label_resultado = Label(menu_inicial,
                        textvariable=final)

# layout
label1.grid()
textbox1.grid()
botao1.grid()
label_resultado.grid()

menu_inicial.mainloop()
