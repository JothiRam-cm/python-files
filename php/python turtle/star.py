import turtle
win=turtle.Screen()
win.setup(800,800)
win.bgcolor("black")
win.title("ct7")

d=turtle.Turtle()
d.speed("fastest")
d.pencolor("gold")
d.pensize(5)
d.hideturtle()
d.penup()
d.setpos(0,0)
d.pendown()
for i in range(360):
    d.forward(2*i)
    d.left(144)