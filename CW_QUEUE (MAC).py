import tkinter as tk
from tkinter import messagebox

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self, x):
        self.element.append(x)

    def dequeue(self):
        if self.element:
            return self.element.pop(0)
        else:
            return None

    def display_Queue(self):
        print("Elements in the Queue:")
        return self.element

#========GUI=========
queue = Queue()

def enqueue_item():
    value = entry.get()
    if value == "":
        messagebox.showwarning("Warning", "Enter a value first!")
        return
    queue.enqueue(value)
    entry.delete(0, tk.END)
    update_display()

def dequeue_item():
    removed = queue.dequeue()
    if removed is None:
        messagebox.showinfo("Info", "Queue is empty!")
    else:
        messagebox.showinfo("Removed Item", "Dequeued: Removed")
    update_display()

def update_display():
    items = queue.display_Queue()
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)

root = tk.Tk()
root.title("Queue System")

#========Widgets=========
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
