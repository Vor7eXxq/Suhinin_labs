import turtle
t = turtle.Turtle()
t.speed(3)
side_length = 120
colors = ["red", "green", "blue", "black"]
t.penup()
t.goto(-side_length/2, side_length/2)
t.pendown()
for i in range(4):
    t.color(colors[i])
    t.forward(side_length)
    t.right(90)
t.penup()
t.goto(0, 0)
for i in range(4):
    t.color(colors[i])
    t.setheading(45 - 90*i)
    radius = (side_length/2) * (2**0.5)
    t.pendown()
    t.forward(radius)
    t.penup()
    t.goto(0,0)
t.hideturtle()
turtle.done()