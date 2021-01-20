from tkinter import *


class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self['height'] = 200
        self['width'] = 400
        self['bg'] = 'green'

menu_inicial = Tk()
menu_inicial.title('SELF INIT E SUPER')
menu_inicial.resizable(False, False)

frm1 = MinhaFrame(menu_inicial).grid()

menu_inicial.mainloop()
