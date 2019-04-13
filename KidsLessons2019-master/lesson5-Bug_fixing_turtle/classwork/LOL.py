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
i = 0
while i < 12:
    i = i + 1
    t.pendown()
    t.forward(150)
    t.left(150)
    if abs(t.pos()) < 1:
        break
t.end_fill()
t.penup()

def draw_square(color,x = 0,y = 0):
    t.goto(x, y)
    t.begin_fill()
    t.pendown()
    t.color(color, 'red')
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.fillcolor(color)
    t.penup()
    t.end_fill()


def draw_flower(x, y,  size=60):
    draw_square('purple', x - size, y-size)
    draw_square('orange', x - size, y+size)
    draw_square('pink', x + size, y+size)
    draw_square('blue', x + size, y-size)
    draw_square('yellow', x, y)

draw_flower(0,-200,50)

draw_flower(150,-20,101)

draw_flower(-200,100,201)

draw_flower(100,100,20)

t.color('blue')
t.shape("turtle")
t.hideturtle()

startX = -100
startY = 200



t.exitonclick()