import turtle
win=turtle.Screen()
win.setup(800,800)
win.bgcolor("black")
win.title("fan")

d=turtle.Turtle()
d.speed("fastest")
d.pensize(5)

color=("orange","white","navyblue","GREEN")

for i in range(0,180,1):
    d.goto(0,0)
    d.pencolor(color[i % len(color)])
    d.setheading(2*i)
    d.forward(200)
    d.left(30)
    d.forward(25)
    d.left(30)
    d.forward(25)
d.goto(0,0)    
