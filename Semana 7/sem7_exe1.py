from tkinter import Tk, Label, PhotoImage


root = Tk()
photo = PhotoImage(file='computer.gif').subsample(2)
hello = Label(master=root, image=photo, width=300, height=180)
## pack() faz o enpacotamento
hello.pack()
root.mainloop()
