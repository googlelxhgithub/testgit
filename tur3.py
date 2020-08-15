import turtle
import math

bob = turtle.Turtle()

bob.color("red", "yellow")
bob.speed(10)

# bob.begin_fill()
for i in range(100):
    bob.forward(math.sqrt(i)*10)
    bob.left(i%90)
# bob.end_fill()

turtle.done()