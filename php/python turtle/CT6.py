import turtle
win=turtle.Screen()
win.setup(300,300)
win.bgcolor("black")
win.title("ct18")

d=turtle.Turtle()
d.speed("slowest")
d.pencolor("gray")
d.pensize(5)
d.setpos(0,-100)
color=("orange","white","blue","darkgreen")

for c in color:
    d.fillcolor(c)
    d.begin_fill()
    d.circle(100)
    d.end_fill()
    