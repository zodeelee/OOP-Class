import tkinter as tk
from tkinter import messagebox

class Stack:
    def __init__(self):
        self.element = []

    def push(self):
        self.element.append(Stack.get(1.0,"end-1c"))

    def pop(self):
        self.element.pop()

    def displayStack(self):
        print("Elements in the Stack:")
        return self.stack_out

#====Stack=====
queue = Stack()

def enqueue_item():
    value = entry.get()
    queue.enqueue(value)
    entry.delete(0, tk.END)
    update_display()

def dequeue_item():
    removed = queue.dequeue()


def update_display():
    items = queue.display_Queue()
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)


#========WIDGETS=========
# Start_up Menu
root = tk.Tk()
root.title("Queue System")

# Input Box
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, padx=10, pady=10)

# Buttons
enqueue_btn = tk.Button(root, text="Enqueue", width=15, command=enqueue_item)
enqueue_btn.grid(row=0, column=1, padx=5)

dequeue_btn = tk.Button(root, text="Dequeue", width=15, command=dequeue_item)
dequeue_btn.grid(row=1, column=1, padx=5)

# Display Box
listbox = tk.Listbox(root, width=40, height=10)
listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()