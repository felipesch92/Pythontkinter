from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Título')
#menu_inicial.geometry('500x300')

bd = 10

label1 = Label(
    menu_inicial,
    text='Frase1\n\nFrase2',
    font='Arial 20',
    bd=bd,
    relief='solid')
label1.pack()

label2 = Label(
    menu_inicial,
    text='Frase',
    font='Arial 20',
    bd=bd,
    relief='flat')
label2.pack()

label3 = Label(
    menu_inicial,
    text='Olá mundo!',
    font='Arial 20',
    bd=bd,
    relief='raised')
label3.pack()

label4 = Label(
    menu_inicial,
    text='Felipe Schmaedecke',
    font='Arial 20',
    bd=bd,
    relief='sunken')
label4.pack()

label5 = Label(
    menu_inicial,
    text='Sistema 2.0',
    font='Arial 20',
    bd=bd,
    relief='groove')
label5.pack()

label6 = Label(
    menu_inicial,
    text='Controle de Usuário',
    font='Arial 20',
    bd=5,
    relief='ridge')
label6.pack()

menu_inicial.mainloop()
