# 请使用Python3编程，画出一个如下图所示坐标系。

import turtle

myPen = turtle.Pen()

for i in range(4):
    for j in range(3):
        myPen.forward(100)
        myPen.dot(5)
    myPen.goto(0,0)
    myPen.left(90)

myPen.dot(5)
myPen.hideturtle()

turtle.done()