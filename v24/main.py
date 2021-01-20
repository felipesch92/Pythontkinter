from tkinter import *


class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()

        self.text_nome_text = StringVar()
        self.lbl_nome_text = StringVar()

        self.text_nome_text.set('Felipe')

        self['bd'] = 2
        self['relief'] = 'solid'

        self.lbl_nome = Label(self, textvariable=self.lbl_nome_text)
        self.text_nome = Entry(self, textvariable=self.text_nome_text)
        self.btn_clique = Button(self,
                            text='Clique',
                            command=self.executar).grid(row=1)
        self.lbl_nome.grid(row=2)
        self.text_nome.grid(row=0)

    def executar(self):
        self.lbl_nome_text.set('Olá, ' + self.text_nome.get() + '!')


menu_inicial = Tk()
menu_inicial.title('Frame e instanciação')
menu_inicial.geometry('300x150')
menu_inicial.resizable(False, False)

frm_1 = MinhaFrame(menu_inicial).grid()

menu_inicial.mainloop()
