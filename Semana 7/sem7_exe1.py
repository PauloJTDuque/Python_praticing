from tkinter import Tk, Label


root = Tk()
hello = Label(master=root, text='Olá classe!')
## pack() faz o enpacotamento
hello.pack()
root.mainloop()
