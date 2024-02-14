import turtle
win=turtle.Screen()
win.setup(300,300)
win.bgcolor("black")
win.title("ct18")

d=turtle.Turtle()
d.speed("fastest")
d.pencolor("gray")
d.pensize(5)
d.hideturtle()
d.setpos(0,-100)
v= win.textinput("mood input","What's your moode:")
if v=="angrey":
   d.fillcolor("red")
   d.begin_fill()
   d.circle(100)
   d.end_fill()
   
elif v=="sad":
   d.fillcolor("blue")
   d.begin_fill()
   d.circle(100)
   d.end_fill()

elif v=="happy":
   d.fillcolor("yellow")
   d.begin_fill()
   d.circle(100)
   d.end_fill()
   
elif v==None:
   d.fillcolor("white")
   d.begin_fill()
   d.circle(100)
   d.end_fill()
else:
   d.fillcolor("gray")
   d.begin_fill()
   d.circle(100)
   d.end_fill()