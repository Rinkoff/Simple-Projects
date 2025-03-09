import turtle


screen = turtle.Screen()
screen.title("Рисуващата костенурка")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(3)


def move_up():
    pen.setheading(90)
    pen.forward(20)

def move_down():
    pen.setheading(270)
    pen.forward(20)

def move_left():
    pen.setheading(180)
    pen.forward(20)

def move_right():
    pen.setheading(0)
    pen.forward(20)


def change_color():
    colors = ["black","red", "blue", "green", "purple", "orange"]
    pen.color(colors[(colors.index(pen.pencolor()) + 1) % len(colors)])

def clear_screen():
    pen.clear()


screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(change_color, "c")
screen.onkey(clear_screen, "space")

screen.mainloop()