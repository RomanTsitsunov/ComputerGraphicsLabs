from tkinter import *
root=Tk()

x1=100
y1=100
x2=400
y2=300

def right(event):
    canvas.move(rectangl, 10, 0)

def left(event):
    canvas.move(rectangl, -10, 0)

def up(event):
    canvas.move(rectangl, 0, -10)

def down(event):
    canvas.move(rectangl, 0, 10)

def pgdown(event):
    global index
    index = (index - 1) % 5
    canvas.itemconfig(rectangl, fill = colors[index])

def pgup(event):
    global index
    index = (index + 1) % 5
    canvas.itemconfig(rectangl, fill = colors[index])

def escape(event):
    root.destroy()

index = 0;
colors = ['red', 'yellow', 'green', 'blue', 'black']

canvas = Canvas(root, width=500, height=500)
rectangl = canvas.create_rectangle(x1,y1,x2,y2)
canvas.focus_set()
canvas.pack()

canvas.bind("<Right>", right)
canvas.bind("<Left>", left)
canvas.bind("<Up>", up)
canvas.bind("<Down>", down)
canvas.bind("<Next>", pgdown)
canvas.bind("<Prior>", pgup)
canvas.bind("<Escape>", escape)

root.mainloop()