#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Техническое задание:
На основе цветочка из квадратов, сделанного в первой итерации,
нарисовать картину из этого цветочка и солнышка.
Солнышко такое как тут, подойдет https://docs.python.org/3.7/library/turtle.html
В будущем ожидаю увидеть поле из разных цветов. Может, сделать цветок красивее.
"""

import turtle as t


t.penup()
t.goto(-200, 200)
a = abs(t.pos())
t.speed(400)
t.color('red', 'yellow')
t.begin_fill()
while True:
    t.forward(150)
    t.left(150)
    if abs(t.pos()) < 1:
        break
t.end_fill()

def draw_square(color):
    t.begin_fill()
    t.pendown()
    t.color(color, 'red')
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.fillcolor(color)
    t.penup()
    t.end_fill()

startX = -200
startY = 150


t.goto(60,60)
draw_square('purple')
t.goto(-60,-60)
draw_square('orange')
t.goto(-60,60)
draw_square('pink')
t.goto(60,-60)
draw_square('blue')
t.goto(0,0)
t.color('blue')
draw_square('yellow')
t.shape("turtle")
t.hideturtle()

startX = -100
startY = 200


t.exitonclick()