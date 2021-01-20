from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Título')
#menu_inicial.geometry('500x300')
menu_inicial.resizable(False, False)

label1 = Label(
    menu_inicial,
    text='label1',
    bg='red',
    font='Arial 20'
)
label2 = Label(
    menu_inicial,
    text='Tamara Cardoso Gruetzmann',
    bg='green',
    font='Arial 20'
)
label3 = Label(
    menu_inicial,
    text='Felipe Schmaedecke',
    bg='blue',
    font='Arial 20'
)

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

btn1 = Button(
    menu_inicial,
    text='Click1'
)
btn2 = Button(
    menu_inicial,
    text='Clique para beijar o tigre'
)
btn3 = Button(
    menu_inicial,
    text='Click3'
)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)

menu_inicial.mainloop()
