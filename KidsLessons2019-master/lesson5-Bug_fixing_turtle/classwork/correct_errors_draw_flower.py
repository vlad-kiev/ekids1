#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Техническое задание:
Нарисовать цветочек из квадратов,
чтоб серединка была желтой,
а лепестки других цветов
"""

import turtle as t


#t.goto(curX, curY)
#t.fillcolor('red')

def draw_square(color):
    t.color(color)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)

draw_square("black")

t.left(45)
t.forward(80)

draw_square("green")

t.left(180)
t.forward(100)

draw_square("red")

t.shape("turtle")

#t.hideturtle()

t.speed(30)

t.exitonclick()


