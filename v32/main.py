from tkinter import *


def file_new_click():
    print('File -> New')

menu_inicial = Tk()
menu_inicial.title('Adicionar menu à aplicação')

meu_menu = Menu(menu_inicial)

# Menu File
file_menu = Menu(meu_menu, tearoff=0)
file_menu.add_command(label='New',
                      command=file_new_click)
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_separator()
file_menu.add_command(label='Exit')
meu_menu.add_cascade(label='File',
                     menu=file_menu)

# Menu Edit
file_edit = Menu(meu_menu, tearoff=0)
file_edit.add_command(label='Copy')
file_edit.add_command(label='Paste')
file_edit.add_command(label='Select All')
meu_menu.add_cascade(label='Edit', menu=file_edit)

# Menu about
meu_menu.add_command(label='About')

menu_inicial.config(menu=meu_menu)

menu_inicial.mainloop()
