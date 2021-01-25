from tkinter import *


def vervalor():
    print(slide.get())


menu_principal = Tk()
menu_principal.title('Scale')
menu_principal.geometry('300x200')

slide = Scale(menu_principal,
              from_=0,
              to=100,
              orient=HORIZONTAL,
              resolution=0.5)
slide.pack()

btn_ver_valor = Button(menu_principal,
                  text='Ver Valor',
                  command=vervalor)
btn_ver_valor.pack()

menu_principal.mainloop()
