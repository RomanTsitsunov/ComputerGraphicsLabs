from tkinter import *

root=Tk()

canvas = Canvas(root,width=500, height=500)
canvas.focus_set()
canvas.pack(side=LEFT)
manage=Frame(root,width=200, height=500)

manage.pack(side=RIGHT)

label1=Label(manage,text="x1")
text1=Entry(manage)
label2=Label(manage,text="y1")
text2=Entry(manage)
label3=Label(manage,text="x2")
text3=Entry(manage)
label4=Label(manage,text="y2")
text4=Entry(manage)
label5=Label(manage,text="dx")
text5=Entry(manage)
label6=Label(manage,text="dy")
text6=Entry(manage)

label1.pack()
text1.pack()
label2.pack()
text2.pack()
label3.pack()
text3.pack()
label4.pack()
text4.pack()
label5.pack()
text5.pack()
label6.pack()
text6.pack()


def draw(event):
    """Считывает координаты и если формат верный - рисует прямоугольник"""
    errorlabel.config(text="")
    if text1.get() == "":
        x1 = 100
    else:
        x1 = (text1.get())
    if text2.get() == "":
        y1 = 100
    else:
        y1 = (text2.get())
    if text3.get() == "":
        x2 = 400
    else:
        x2 = (text3.get())
    if text4.get() == "":
        y2 = 300
    else:
        y2 = (text4.get())
    global rectangl
    try:
        rectangl = canvas.create_rectangle(x1, y1, x2, y2)
    except:
        errorlabel.config(text="Неверный формат координат прямоугольника")

def delta():
    """Считывает и возвращает сдвиги по x и по y"""
    if text5.get() == "":
        dx = 10
    else:
        dx = int(text5.get())
    if text6.get() == "":
        dy = 10
    else:
        dy = int(text6.get())
    return dx, dy

def right(event):
    """Если прямоугольник отрисован и верно заданы сдвиги, сдвигает прямоугольник на dx вправо"""
    errorlabel.config(text="")
    try:
        dx, dy = delta()
    except:
        errorlabel.config(text="Неверный формат сдвига")
        return
    try:
        canvas.move(rectangl, dx, 0)
    except:
        errorlabel.config(text="Сначала необходимо создать прямоугольник")

def left(event):
    """Если прямоугольник отрисован и верно заданы сдвиги, сдвигает прямоугольник на dx влево"""
    errorlabel.config(text="")
    try:
        dx, dy = delta()
    except:
        errorlabel.config(text="Неверный формат сдвига")
        return
    try:
        canvas.move(rectangl, -dx, 0)
    except:
        errorlabel.config(text="Сначала необходимо создать прямоугольник")

def up(event):
    """Если прямоугольник отрисован и верно заданы сдвиги, сдвигает прямоугольник на dy вверх"""
    errorlabel.config(text="")
    try:
        dx, dy = delta()
    except:
        errorlabel.config(text="Неверный формат сдвига")
        return
    try:
        canvas.move(rectangl, 0, -dy)
    except:
        errorlabel.config(text="Сначала необходимо создать прямоугольник")

def down(event):
    """Если прямоугольник отрисован и верно заданы сдвиги, сдвигает прямоугольник на dy вниз"""
    errorlabel.config(text="")
    try:
        dx, dy = delta()
    except:
        errorlabel.config(text="Неверный формат сдвига")
        return
    try:
        canvas.move(rectangl, 0, dy)
    except:
        errorlabel.config(text="Сначала необходимо создать прямоугольник")

def pgdown(event):
    """Если прямоугольник отрисован, меняет цвет на предыдущий из списка цветов"""
    errorlabel.config(text="")
    global index
    index = (index - 1) % 5
    try:
        canvas.itemconfig(rectangl, fill = colors[index])
    except:
        errorlabel.config(text="Сначала необходимо создать прямоугольник")

def pgup(event):
    """Если прямоугольник отрисован, меняет цвет на следующий из списка цветов"""
    errorlabel.config(text="")
    global index
    index = (index + 1) % 5
    try:
        canvas.itemconfig(rectangl, fill = colors[index])
    except:
        errorlabel.config(text="Сначала необходимо создать прямоугольник")

def escape(event):
    """Закрывает программу"""
    root.destroy()

index = 0;
colors = ['red', 'yellow', 'green', 'blue', 'black']

butDraw=Button(manage, text="Рисовать", width=12)
butDraw.bind("<Button-1>", draw)
butDraw.pack()

errorlabel=Label(manage, text="",fg="red")
errorlabel.pack()

canvas.bind("<Right>", right)
canvas.bind("<Left>", left)
canvas.bind("<Up>", up)
canvas.bind("<Down>", down)
canvas.bind("<Next>", pgdown)
canvas.bind("<Prior>", pgup)
canvas.bind("<Escape>", escape)

root.mainloop()