from turtle import *

def draw_shape(sides, length):
    begin_fill()
    for _ in range(sides):
        forward(length)
        right(360 / sides)
        #fillcolor("green")
    end_fill()

def draw_matrix(matrix):
    startx = -200
    starty = 200
    shapeSide = 50
    for row in range(len(matrix)) :
        for col in range(len(matrix[row])):
            cell = matrix[row][col]
            if cell == 1 :
                fillcolor("violet")
            else:
                fillcolor("red")
                curx = startx + shapeSide * col
                cury = starty - shapeSide * row
                goto(curx, cury)
                draw_shape(4, shapeSide)

matrix = [
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 1, 0],
          [0, 0, 1, 0, 0, 1, 0, 0],
          [0, 0, 0, 1, 1, 0, 0, 0]
         ]

setup (width=600, height=600, startx=0, starty=0)
color('yellow')
# shape("turtle")
hideturtle()

speed(30)
draw_matrix(matrix)

exitonclick()