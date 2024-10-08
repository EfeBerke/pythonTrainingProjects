

import turtle

turtle.pensize(5)
turtle.pencolor("Red")


def draw_square():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)


turtle.goto(0, 0)
turtle.left(150)
draw_square()

turtle.pencolor("Blue")
turtle.right(20)
draw_square()

turtle.pencolor("Green")
turtle.right(20)
draw_square()

turtle.done()
