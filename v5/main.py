from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Título')
menu_inicial.geometry('500x300')

label1 = Label(menu_inicial,
               text='Este é o label 1',
               bg='red',
               font='Arial 20 bold italic')
label1.pack()

label2 = Label(menu_inicial,
               text='Este é o label 2',
               bg='blue',
               font='Arial 25 italic')
label2.pack()

label3 = Label(menu_inicial,
               text='Este é o label 2',
               bg='green',
               font='Verdana 42 bold')
label3.pack()

menu_inicial.mainloop()
