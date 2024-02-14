import turtle
win=turtle.Screen()
win.setup(800,800)
win.bgcolor("black")
win.title("fan")

d=turtle.Turtle()
d.speed("fastest")
d.pensize(5)

color=("GREEN","navyblue","white","orange")

for x in range(-400,400,75):
    r=1
    for y in range(300,-300,-75):
        d.penup()
        d.goto(x,y)
        d.pendown()
        d.pencolor(color[r % len(color)])
        d.fillcolor(color[r % len(color)])
        d.begin_fill()
        d.circle(25)
        d.end_fill()
        r=r+1