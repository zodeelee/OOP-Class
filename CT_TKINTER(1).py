#VISUAL DEMONSTRATION OF WHAT A SIMPLE TKINTER LABEL/GRID LOOKS LIKE
import tkinter as tk

root = tk.Tk()
root.title("Grid Demo")

# These labels will show up as colored squares
label1 = tk.Label(root, text="A", bg="lightblue", width=10, height=3)
label2 = tk.Label(root, text="B", bg="lightgreen", width=10, height=3)
label3 = tk.Label(root, text="C", bg="lightpink", width=10, height=3)

# Try changing the row/column numbers and watch what happens!
label1.grid(row=1, column=0)
label2.grid(row=1, column=1)
label3.grid(row=3, column=0)

root.mainloop()