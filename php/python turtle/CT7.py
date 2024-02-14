import turtle
win=turtle.Screen()
win.setup(300,300)
win.bgcolor("black")
win.title("ct7")

d=turtle.Turtle()
d.speed("slowest")
d.pencolor("gray")
d.pensize(5)
d.penup()
d.setpos(0,-100)
d.pendown()
color=("orange","white","blue","darkgreen")
c=0
while c <= len(color):
    d.fillcolor(color[c])
    d.begin_fill()
    d.circle(100)
    d.end_fill()
    c=c+1