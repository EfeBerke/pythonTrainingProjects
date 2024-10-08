

import turtle

turtle.pensize(3)
turtle.pencolor("Blue")

# Draw your star shape in the following editable code block
"""
i = 0
while i < 5:
    turtle.forward(100)
    turtle.right(144)
    i += 1
"""

# Draw your Hexagon shape in the following editable code block
"""
i = 0
while i < 6:
    turtle.forward(100)
    turtle.right(60)
    i += 1
"""

# Draw your Spiral shape in the following editable code block
"""
a = 0
while a < 100:
    turtle.forward(a)
    turtle.left(15)
    a += 1
turtle.done()
"""

# Draw your Olimpia shape in the following editable code block
"""
def drawing_ring(color, x_coordinate, y_coordinate):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x_coordinate, y_coordinate)
    turtle.pendown()
    turtle.circle(30)


turtle.circle(30)
drawing_ring("Yellow", 35, -15)
drawing_ring("Black", 70, 0)
drawing_ring("Green", 105, -15)
drawing_ring("Red", 140, 0)


turtle.done()
"""
# Draw your Chain of Rings shape in the following editable code block
# Same logic with Olimpia shape (Playing with values)
