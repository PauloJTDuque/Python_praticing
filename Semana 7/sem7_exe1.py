from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM


root = Tk()
photo = PhotoImage(file='computer.gif').subsample(2)
image=Label(master=root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=("Courier", 18), text='Olá Alunos UNIVESP!')
## pack() faz o enpacotamento
text.pack(side=BOTTOM)
root.mainloop()
