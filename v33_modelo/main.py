from tkinter import *


def salvar_formulario(nome, cpf):
    print(f'Nome: {nome}')
    print(f'CPF: {cpf}')
    top.destroy()


def abrir_formulario():
    # top level
    global top
    top = Toplevel()
    top.title('Novo Formulário')
    top.geometry('200x100')

    sv_nome = StringVar()
    sv_cpf = StringVar()
    # Widgets
    lb1 = Label(top,
                text='Nome: ')
    lb2 = Label(top,
                 text='CPF: ')
    txt_nome = Entry(top,
                     textvariable=sv_nome)
    txt_cpf = Entry(top,
                    textvariable=sv_cpf)
    btn_salvar = Button(top,
                        text='Salvar',
                        command=lambda: salvar_formulario(sv_nome.get(), sv_cpf.get()))

    #Adicionando na tela
    lb1.grid(row=0, column=0)
    txt_nome.grid(row=0, column=1)
    lb2.grid(row=1, column=0)
    txt_cpf.grid(row=1, column=1)
    btn_salvar.grid(row=2, columnspan=2)

menu_inicial = Tk()
menu_inicial.title('Top Level')
menu_inicial.geometry('300x200')
btn_novo = Button(menu_inicial,
                  text='Novo',
                  command=abrir_formulario)
btn_novo.pack()

menu_inicial.mainloop()
