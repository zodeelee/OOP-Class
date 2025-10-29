#calculator

import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("500x500")

answer = Text(width=35, height=2)
answer.place(x=100, y=100)

def show(self,x): #myfunction
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)

        else:
            answer.insert(tk.INSERT, x)

        if x == "C":
            answer.delete(1.0, END)
    except:
        answer.insert(tk.INSERT, END)

B1 = Button(top, text="1", width=10, height=5, command=lambda: show("1"))
B1.place(x=100, y=150)

B2 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))
B2.place(x=200, y=150)

B3 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))
B2.place(x=200, y=150)

B4 = Button(top, text="4", width=10, height=5, command=lambda: show("4"))
B4.place(x=100, y=350)

B5 = Button(top, text="5", width=10, height=5, command=lambda: show("5"))
B5.place(x=200, y=350)

B6 = Button(top, text="6", width=10, height=5, command=lambda: show("6"))
B6.place(x=300, y=350)

B7 = Button(top, text="7", width=10, height=5, command=lambda: show("7"))
B7.place(x=100, y=250)

B8 = Button(top, text="8", width=10, height=5, command=lambda: show("8"))
B8.place(x=200, y=250)

B9 = Button(top, text="9", width=10, height=5, command=lambda: show("9"))
B9.place(x=300, y=250)

B0 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))
B2.place(x=200, y=150)

Badd = Button(top, text="+", width=10, height=5, command=lambda: show("+"))
Badd.place(x=300, y=150)

Bsub = Button(top,text="-", width=10, height=5, command=lambda: show("-"))
Bsub.place(x=400, y=150)

Bmul = Button(top, text="x", width=10, height=5, command=lambda: show("x"))
Bmul.place(x=400, y=250)

Bdiv = Button(top, text="/", width=10, height=5, command=lambda: show("/"))
Bdiv.place(x=400, y=150)

Bclear = Button(top, text="C", width=10, height=5, command=lambda: show("C"))
Bclear.place(x=100, y=150)

Bparenthesis = Button(top, text="( )", width=10, height=5, command=lambda: show("( )"))
Bparenthesis.place(x=200, y=150)

Bpercent = Button(top, text="%", width=10, height=5, command=lambda: show("%"))
Bpercent.place(x=300, y=150)


top.mainloop()