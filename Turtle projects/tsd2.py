import turtle
import random


screen = turtle.Screen()
screen.title("treasure hunt")
screen.setup(width=600, height=600)
screen.bgcolor("lightblue")


player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()

treasure = turtle.Turtle()
treasure.shape("circle")
treasure.color("gold")
treasure.penup()
treasure.goto(random.randint(-250, 250), random.randint(-250, 250))


obstacles = []
for _ in range(50):
    obs = turtle.Turtle()
    obs.shape("square")
    obs.color("red")
    obs.penup()
    obs.goto(random.randint(-250, 250), random.randint(-250, 250))
    obstacles.append(obs)


def move_up():
    y = player.ycor()
    player.sety(y + 20)

def move_down():
    y = player.ycor()
    player.sety(y - 20)

def move_left():
    x = player.xcor()
    player.setx(x - 20)

def move_right():
    x = player.xcor()
    player.setx(x + 20)

screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

def check_collision():
    if player.distance(treasure) < 20:
        player.goto(0, 0)
        treasure.goto(random.randint(-250, 250), random.randint(-250, 250))
        print("Поздравления! Намери съкровището!")

    for obs in obstacles:
        if player.distance(obs) < 20:
            player.goto(0, 0)
            print("Опа! Удари препятствие! Опитай пак.")

while True:
    screen.update()
    check_collision()