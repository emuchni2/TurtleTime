import math
import turtle

# fractalartmaker.drawFractal(fractalartmaker.drawFilledSquare, 600,
#     [{'sizeChange': 0.8, 'yChange': 0.1, 'angleChange': -10},
#      {'sizeChange': 0.8, 'yChange': -0.1, 'angleChange': 10}])


def drawTriangleOutline(size, depth):
    size = int(size)

    # Move the turtle to the top of the equilateral triangle:
    height = size * math.sqrt(3) / 2
    turtle.penup()
    turtle.left(90)  # Turn to face upwards.
    turtle.forward(height * (2/3))  # Move to the top corner.
    turtle.right(150)  # Turn to face the bottom-right corner.
    turtle.pendown()

    # Draw the three sides of the triangle:
    for i in range(3):
        turtle.forward(size)
        turtle.right(120)


fractalartmaker.drawFractal(drawTriangleOutline, 20, [{'sizeChange': 1.05, 'angleChange': 7}], 80)
