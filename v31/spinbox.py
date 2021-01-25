from tkinter import *


def mostrar_valor():
    print(f'S1: {s1.get()}')
    print(f'S2: {s2.get()}')
    print(f'S3: {s3.get()}')


menu_inicial = Tk()
menu_inicial.title('SpinBox')
menu_inicial.geometry('300x200')


s1 = Spinbox(menu_inicial,
             from_=0,
             to=10)
s2 = Spinbox(menu_inicial,
             values=(10, 20, 30, 40, 50),
             wrap=True)
s3 = Spinbox(menu_inicial,
             values=('Felipe', 'Fernando', 'Dolores'),
             wrap=True)
btn_ok = Button(menu_inicial,
                text='Clique',
                command=mostrar_valor)

s1.grid(row=0, column=0)
s2.grid(row=1, column=0)
s3.grid(row=2, column=0)
btn_ok.grid(row=3, column=0)

menu_inicial.mainloop()
