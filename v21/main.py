from tkinter import *


def mostrar():
    endereco.set(text_box_endereco.get() + ' - ' + text_box_data_nasc.get())


def acessar():
    login.set(text_box_login.get() + ' - ' + text_box_senha.get())

menu_inicial = Tk()
menu_inicial.title('Duas frames')

frame_login = Frame(menu_inicial)
frame_dados = Frame(menu_inicial)

endereco = StringVar()
login = StringVar()

# widgets
lbl_1 = Label(frame_login,
              text='Login:')
lbl_2 = Label(frame_login,
              text='Senha:')
lbl_endereco = Label(frame_login,
                     textvariable=endereco)
text_box_login = Entry(frame_login)
text_box_senha = Entry(frame_login)
btn_acessar = Button(frame_login,
                     text='Acessar',
                     command=acessar)

lbl_3 = Label(frame_dados,
              text='Data Nascimento:')
lbl_4 = Label(frame_dados,
              text='Endereço:')
lbl_login = Label(frame_dados,
                  textvariable=login)
text_box_data_nasc = Entry(frame_dados)
text_box_endereco = Entry(frame_dados)
btn_salvar = Button(frame_dados,
                    text='Salvar',
                    command=mostrar)

# layout
lbl_1.grid(row=0, column=0)
lbl_2.grid(row=1, column=0)
text_box_login.grid(row=0, column=1)
text_box_senha.grid(row=1, column=1)
lbl_endereco.grid(row=2, columnspan=2)
btn_acessar.grid(row=3, columnspan=2)

lbl_3.grid(row=0, column=0)
lbl_4.grid(row=1, column=0)
text_box_data_nasc.grid(row=0, column=1)
text_box_endereco.grid(row=1, column=1)
lbl_login.grid(row=2, columnspan=2)
btn_salvar.grid(row=3, columnspan=2)

frame_login.grid(row=0, column=0)
frame_dados.grid(row=0, column=1)

menu_inicial.mainloop()
