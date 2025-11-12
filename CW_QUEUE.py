import tkinter as tk
from tkinter import messagebox


class Queue:
    def __init__(self):
        self.elements = []

    def enqueue (self, value):
        self.elements.append(value)

    def dequeue (self):
        if self.elements:
            self.element.pop(0)
        else:
            return None

    def display (self):
        print("Elements in the Queue:")
        for i in self.element:
            print(i)

class QueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue System: (Enqueue, Dequeue, Display")
        self.root.geometry("400x250")

        self.queue = Queue()

        #USER INPUT
        self.input_var = tk.StringVar()
        tk.Label(root, text="Enter value:").place(x=60, y=20)
        tk.Entry(root, textvariable=self.input_var, width=20).place(x=150, y=20)

        #BUTTONS
        tk.Button(root, text="Enqueue", command=self.enqueue_action).place(x=60, y=60)
        tk.Button(root, text="Dequeue", command=self.dequeue_action).place(x=150, y=60)
        tk.Button(root, text="Display", command=self.update_display).place(x=240, y=60)

        # Display area
        self.answer = tk.Text(root, width=40, height=5)
        self.answer.place(x=60, y=110)
        self.answer.config(state=tk.DISABLED)

#======= Main Code =======

#GUI Window Setup
top = tk.Tk()
top.title("GUI Queue")
top.geometry("400x400")

answer = tk.Text(width=35, height=2)
answer.place(x=60, y=60)

#Main Code
q1 = Queue()
q2 = Queue()

# Display Box
#answer = tk.Text(top, width=35, height=2)
#answer.place(x=60, y=60)

#read-only
#answer.config(state=tk.DISABLED)

#input_var = tk.StringVar()
#input_entry = tk.Entry(top, textvariable=input_var, width=15)
#input_entry.place(x=60, y=20)

top.mainloop()
