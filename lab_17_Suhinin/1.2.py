import turtle

screen = turtle.Screen()
screen.bgcolor("lightcyan")
screen.title("Шахівниця 4х4")

t = turtle.Turtle()
t.speed(0)

grid_size = 4
cell_size = 40
color1 = "darkgray"
color2 = "white"

start_x = - (grid_size * cell_size) / 2
start_y = (grid_size * cell_size) / 2

def draw_square(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

for row in range(grid_size):
    for col in range(grid_size):
        x = start_x + col * cell_size
        y = start_y - row * cell_size

        t.penup()
        t.goto(x, y)
        t.pendown()

        if (row + col) % 2 == 0:
            current_color = color1
        else:
            current_color = color2

        draw_square(cell_size, current_color)

t.hideturtle()
turtle.done()