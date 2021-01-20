from tkinter import *

# GUI
menu_inicial = Tk()
menu_inicial.title('Introdução a frame widget')

#widgets

frame_login = Frame(menu_inicial)


label_usr = Label(frame_login, text='Usuário: ')
label_pwd = Label(frame_login, text='Senha: ')
text_usr = Entry(frame_login)
text_pwd = Entry(frame_login)
btn_entrar = Button(frame_login,
                    text='Entrar')

#layouts
label_usr.grid(row=0, column=0)
label_pwd.grid(row=1, column=0)
text_usr.grid(row=0, column=1)
text_pwd.grid(row=1, column=1)
btn_entrar.grid(row=2, column=1, columnspan=2)

# Colocado frame login no menu_inicial
frame_login.grid()

menu_inicial.mainloop()
