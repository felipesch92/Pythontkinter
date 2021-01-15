from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Título')
menu_inicial.geometry('500x300')

#nome = input('Digite seu nome: ').upper()

label2 = Label(menu_inicial)
label2['text'] = 'Felipe Schmaedecke'
label2['font'] = 'Arial 20'
label2['bd'] = 1
label2['relief'] = 'solid'
label2.pack()

for item in label2.keys():
    print(f'{item} : {label2[item]}')

menu_inicial.mainloop()
