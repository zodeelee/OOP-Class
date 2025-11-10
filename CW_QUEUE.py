#CW_QUEUE.py

import tkinter as tk
from tkinter import *


class Queue:
    def __init__(self):
        self.element = []
    def enqueue (self):
        self.element.append(input("Enter:"))
        valueTxt = text()
        x = valueTxt.get(1.0, "end-1c")
        self.element.append(x)
    def dequeue (self):
        self.element.remove(0)
    def display (self):
        print("Elements in the Queue:")
        for i in self.element:
            print(i)
#=======================

#=======Main=Code=======

# GUI Window Setup
top = tk.Tk()
top.title("GUI Queue")
top.geometry("400x200")

answer = Text(width=35, height=2)
answer.place(x=60, y=60)

# Queue Initilization
q1 = Queue()
#q2 = Queue

# Display Box
answer = tk.Text(top, width=35, height=2)
answer.place(x=60, y=60)

#read-only
answer.config(state=tk.DISABLED)

input_var = tk.StringVar()
input_entry = tk.Entry(top, textvariable=input_var, width=15)
input_entry.place(x=60, y=20)

top.mainloop()