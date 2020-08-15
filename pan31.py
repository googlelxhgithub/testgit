# 请使用Python3编程，画出如下图形。

import turtle
myPen = turtle.Pen()
myPen.speed(0)
myPen.pensize()
myPen.pencolor("red")
myPen.penup()
myPen.goto(-50, -50)
myPen.down()


myPen.forward(100)
myPen.left(90)
myPen.forward(100)
myPen.left(90)
myPen.forward(100)
myPen.left(90)
myPen.forward(100)

myPen.penup()
myPen.forward(100)
myPen.pendown()
myPen.forward(100)
myPen.left(90)
myPen.forward(100)
myPen.left(90)
myPen.forward(100)
myPen.left(90)
myPen.forward(100)
myPen.left(90)

turtle.done()

