from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Message')

msg = Message(menu_inicial,
              text='Este é o texto do message widget',
              width=100,
              bg='blue')
msg.pack()

menu_inicial.mainloop()
