import turtle
win=turtle.Screen()
win.setup(1000,800)
win.title("CT2")
win.bgcolor("black")

d=turtle.Turtle()
d.speed("slow")
d.pensize(10)
d.pencolor("darkgreen")
d.penup()
d.setpos(0,-250)
d.fillcolor("green")
d.begin_fill()
d.pendown()
d.circle(250)
d.end_fill()
d.penup()
d.home()
d.left(10)
d.forward(125)
d.pendown()
d.fillcolor("black")
d.begin_fill()
d.pencolor("black")
d.pensize(2)
d.circle(70)
d.end_fill()
d.penup()
d.home()
d.left(135)

d.goto(-125,125)

d.pencolor("black")
d.pendown()
d.pensize(5)
d.goto(-10,10)
d.penup()
d.goto(-10,125)
d.pendown()
d.goto(-125,10)
d.penup()
d.home()
d.goto(10,-50)
d.right(35)
d.pendown()
d.forward(150)
d.penup()
d.home()
d.goto(10,-50)
d.right(150)
d.pendown()
d.forward(150)
d.speed("slowest")
d.penup()
d.home()
d.reset()
