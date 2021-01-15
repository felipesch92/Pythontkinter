from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')

#Não deixa aumentar ou diminuir o formulário
menu_inicial.resizable(False, False)

# dimensões da janela
l = 500
a = 300

# resolução do nosso sistema
l_screen = menu_inicial.winfo_screenwidth()
a_screen = menu_inicial.winfo_screenheight()

# posição da janela
posx = int(l_screen/2 - l/2)
posy = int(a_screen/2 - a/2)

# Definir a geometry
menu_inicial.geometry(f'{l}x{a}+{posx}+{posy}')

menu_inicial.mainloop()
