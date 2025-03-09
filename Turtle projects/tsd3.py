import turtle
import time
import random

# Настройки на екрана
screen = turtle.Screen()
screen.title("Snаke Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = [turtle.Turtle(shape="square") for _ in range(3)]
for segment in snake:
    segment.color("green")
    segment.penup()

for i in range(len(snake)):
    snake[i].goto(-20 * i, 0)

food = turtle.Turtle(shape="circle")
food.color("red")
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

direction = "stop"

def go_up():
    global direction
    if direction != "down":
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

while True:
    screen.update()
    time.sleep(0.1)

    for i in range(len(snake) - 1, 0, -1):
        x, y = snake[i - 1].pos()
        snake[i].goto(x, y)

    if direction == "up":
        snake[0].sety(snake[0].ycor() + 20)
    if direction == "down":
        snake[0].sety(snake[0].ycor() - 20)
    if direction == "left":
        snake[0].setx(snake[0].xcor() - 20)
    if direction == "right":
        snake[0].setx(snake[0].xcor() + 20)


    if abs(snake[0].xcor()) > 290 or abs(snake[0].ycor()) > 290:
        print("💥 Играта свърши! Удари стената!")
        break

    for segment in snake[1:]:
        if snake[0].distance(segment) < 10:
            print("💥 Играта свърши! Удари себе си!")
            break

    if snake[0].distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        new_segment = turtle.Turtle(shape="square")
        new_segment.color("green")
        new_segment.penup()
        snake.append(new_segment)

screen.mainloop()
