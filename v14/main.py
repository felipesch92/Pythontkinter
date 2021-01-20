from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Login')
#menu_inicial.geometry('200x100')
menu_inicial.resizable(False, False)

lbl_login = Label(
    menu_inicial,
    text='Usuário: '
)
lbl_login.grid(row=0, column=0)

lbl_senha = Label(
    menu_inicial,
    text='Senha: '
)
lbl_senha.grid(row=1, column=0)

tbox_login = Entry(
    menu_inicial
)
tbox_login.grid(row=0, column=1)

tbox_senha = Entry(
    menu_inicial
)
tbox_senha.grid(row=1, column=1)

btn_acessar = Button(
    menu_inicial,
    text='Acessar'
)
btn_acessar.grid(row=2, column=1)

menu_inicial.mainloop()
