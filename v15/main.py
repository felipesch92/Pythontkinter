from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Título')
menu_inicial.geometry('300x200')
menu_inicial.resizable(False, False)

Label(menu_inicial,
      text='texto',
      bg='red').grid(column=0)
Label(menu_inicial,
      text='texto',
      bg='green').grid(column=1)
Label(menu_inicial,
      text='texto',
      bg='yellow').grid(column=2)
Label(menu_inicial,
      text='texto',
      bg='blue').grid(columnspan=3, sticky='we')


menu_inicial.mainloop()
