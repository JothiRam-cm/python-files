import turtle 

win=turtle.Screen()
win.setup(800,600)
win.title("example T1")
#creating turtle
t1=turtle.Turtle()
t1.speed("slowest")
t1.pencolor("blue")
t1.pensize(5)

t1.penup()
t1.setpos(100,100)
t1.pendown()
t1.setpos(-100,100)
t1.setpos(-100,-100)
t1.setpos(100,-100)
t1.setpos(100,100)
