from tkinter import *


# Função
def executar():
    n1.set(t1.get())
    n2.set(t2.get())
    l3['text'] = t3.get()

# GUI
menu_inicial = Tk()
menu_inicial.title('Título')

n1 = StringVar()
n2 = StringVar()

# widgets
t1 = Entry(menu_inicial)
t2 = Entry(menu_inicial)
t3 = Entry(menu_inicial)

l1 = Label(menu_inicial, textvariable=n1)
l2 = Label(menu_inicial, textvariable=n2)
l3 = Label(menu_inicial)
b = Button(menu_inicial,
           text='Executar',
           command=executar)

# Layout
t1.grid()
t2.grid()
t3.grid()
l1.grid()
l2.grid()
l3.grid()
b.grid()
menu_inicial.mainloop()
