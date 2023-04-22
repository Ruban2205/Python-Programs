import turtle
from turtle import *

t = Turtle()
t.color("Black")
t.shape("turtle")
t.speed(0)


def house():
    penup()
    goto(-170, -170)
    pendown()
    pensize(3)
    color("black", "blue")
    begin_fill()
    for i in range(4):
        forward(200)
        left(90)
    end_fill()


def door():
    penup()
    goto(-105, -48)
    pendown()
    color("black", "white")
    begin_fill()
    for i in range(2):
        forward(70)
        right(90)
        forward(122)
        right(90)
    end_fill()


def roof():
    penup()
    goto(-193, 31)
    pendown()
    color('black', 'yellow')
    begin_fill()
    for i in range(3):
        forward(250)
        left(120)
    end_fill()


def man():
    penup()
    goto(180, -170)
    pendown()
    # forward(-200)
    left(90)
    forward(250)
    left(90)
    color("black", "blue")
    begin_fill()
    forward(70)
    left(90)
    forward(30)
    left(90)
    forward(70)
    end_fill()
    left(90)
    forward(120)
    penup()
    goto(210, 190)
    pendown()
    color("black", "yellow")
    begin_fill()
    circle(30)
    end_fill()
    turtle.delay(100)


if __name__ == '__main__':
    house()
    door()
    roof()
    man()
    turtle.mainloop()
