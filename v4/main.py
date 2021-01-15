from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')
menu_inicial.geometry('300x200')

label1 = Label(menu_inicial, text='Este é o label 1.')
label2 = Label(menu_inicial, text='Este é o label 2.')
btn = Button(menu_inicial, text='Executar')

# pack
btn.pack()
label2.pack()
label1.pack()

menu_inicial.mainloop()
