from tkinter import *


def mostrar_valor_a():
    print(f'Grid A: {valor_a.get()}')


def mostrar_valor_b():
    print(f'Grid B: {valor_b.get()}')


def raf2():
    print('Grid A Opção 2')


def rbf3():
    print('Grid B Opção 3')


menu_inicial = Tk()
menu_inicial.title('RadioButton')
menu_inicial.geometry('300x200')

frame_a = Frame(menu_inicial)
frame_a.grid(row=0, column=0)

frame_b = Frame(menu_inicial)
frame_b.grid(row=1, column=0)

valor_a = IntVar()
valor_b = IntVar()

ra_1 = Radiobutton(frame_a,
                   text='Opção A1',
                   variable=valor_a,
                   value=1)
ra_2 = Radiobutton(frame_a,
                   text='Opção A2',
                   variable=valor_a,
                   value=2,
                   command=raf2,
                   indicatoron=0)
ra_3 = Radiobutton(frame_a,
                   text='Opção A3',
                   variable=valor_a,
                   value=3)
ra_1.select()

btn_valor_a = Button(frame_a,
                     text='Ok',
                     command=mostrar_valor_a)

rb_1 = Radiobutton(frame_b,
                   text='Opção A1',
                   variable=valor_b,
                   value=1)
rb_2 = Radiobutton(frame_b,
                   text='Opção A2',
                   variable=valor_b,
                   value=2,
                   indicatoron=0)
rb_3 = Radiobutton(frame_b,
                   text='Opção A3',
                   variable=valor_b,
                   command=rbf3,
                   value=3)
rb_1.select()
btn_valor_b = Button(frame_b,
                     text='Ok',
                     command=mostrar_valor_b)

ra_1.grid(row=0, column=0)
ra_2.grid(row=1, column=0)
ra_3.grid(row=2, column=0)
btn_valor_a.grid(row=3, column=0)

rb_1.grid(row=0, column=0)
rb_2.grid(row=1, column=0)
rb_3.grid(row=2, column=0)
btn_valor_b.grid(row=3, column=0)



menu_inicial.mainloop()
