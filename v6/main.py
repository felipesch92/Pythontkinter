from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Título')

label1 = Label(menu_inicial,
               text='Este é o label 1',
               bg='red',
               font='Arial 20',
               width=30)
label1.pack()

label2 = Label(menu_inicial,
               text='Este é o label 2',
               bg='red',
               font='Arial 40',
               width=30)
label2.pack()

menu_inicial.mainloop()
