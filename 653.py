from tkinter import *
from random import*
from random import randint

def click():
    canvas.delete('all')
    a=random.randint(1,3)
    if a == 1:
     canvas.create_oval(50,50,150,100, outline='black', fill='red')
    elif a== 2:
        canvas.create_polygon(50,50,150,100,300, 70, outline='black', fill='green')
    elif a == 3:
        canvas.create_rectangle(50,50,150,100, outline='black', fill='blue')
root=Tk()
root.geometry('600x600')
root.title('Случайные фигуры')
root.resizable(False, False)

canvas=Canvas(root, width=600, height=500, bg='white')
canvas.pack()
   


canvas.create_oval(30,40,90,100, outline='black', fill='red')
canvas.create_polygon(40,40,130,100,270,80, outline='black', fill='green')
canvas.create_rectangle(50,50,150,100, outline='black', fill='yellow')
b=Button(root, text='click', width=10, height=2, bg='black', fg='white', command=click)
b.pack()
root.mainloop()