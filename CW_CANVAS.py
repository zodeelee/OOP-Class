#=============================
import tkinter
#=============================

root = tkinter.Tk()
root.resizable(False,False)

#create the canvas
myCanvas = tkinter.Canvas(root, bg = "deep sky blue", height=600, width=800)

shape1 = myCanvas.create_oval(150,250,300,400, fill="yellow2")
#shape2 = myCanvas.create_rectangle(200,400,500,500, fill="red")
#shape3 = myCanvas.create_line(300,400,600,700, fill="purple")
#shape4 = myCanvas.create_polygon(200,100,600,700, fill="orange")


myCanvas.pack()
root.mainloop()