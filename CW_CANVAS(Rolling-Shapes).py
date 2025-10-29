import tkinter

root = tkinter.Tk()
root.resizable(False, False)

myCanvas = tkinter.Canvas(root, bg="white", height=600, width=800)

shape1 = myCanvas.create_oval(20, 20, 100, 100, fill="blue")

#initialize the constants xx, yy
xx =yy = -3

def move_shape():
    global xx, yy

    #move the shape with the constanct xx, yy
    myCanvas.move(shape1, xx, yy)

    #get the current coordinates of the shape
    (x1, y1, x2, y2) = myCanvas.coords(shape1)

    #check the boundaries of the coordinates and change the constants xx, yy
    if x1 <= 0 or x2 >= 800:
        xx = -xx

    if y1 <= 0 or y2 >= 600:
        yy = -yy

    #call the function recursively
    myCanvas.after(30, move_shape)


#in the main program call the function move_shape()
myCanvas.after(10,move_shape())

myCanvas.pack()
root.mainloop()