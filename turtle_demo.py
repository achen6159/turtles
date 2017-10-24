from turtle import *

annie = Turtle()
anders = Turtle()
saleem = Turtle()
nathan = Turtle()

annie.shape("turtle")

anders.shape("turtle")

saleem.shape("turtle")

nathan.shape("turtle")

def draw_star(name, x, y, points, line, fill):
    name.penup()
    name.goto(x, y)
    name.pendown()

    turn = 180 - (360 / points)

    name.color(line, fill)

    name.begin_fill()

    for i in range(points):
        name.forward(200)
        name.left(turn)
        
    name.end_fill()
    
colormode(255)

anders.speed(100)
draw_star(anders, 50, 0, 36,(199, 21,133), (153, 50, 204))
annie.speed(100)
draw_star(annie, 0, 0, 36,(255, 218, 185), (0, 191, 255))
saleem.speed(100)
draw_star(saleem, -50, 0, 36,(135, 206, 250), (60, 179, 113))
nathan.speed(100)            
draw_star(nathan, -100, 0, 36,(0, 191, 255), (255, 215, 0))
annie.speed(100)
draw_star(annie, -150, 0, 36, (124, 252, 0), (255, 69, 0))
saleem.speed(100)
draw_star(saleem, -200, 0, 36, (0, 206, 209), (255, 0, 0))


mere = Turtle()
mere.shape("turtle")

def blue():
    mere.color(65, 105, 225)
def green():
    mere.color(50, 205, 50)
def purple():
    mere.color(148, 0, 211)

def up_arrow():
    mere.forward(50)

def left_arrow():
    mere.left(45)

def right_arrow():
    mere.right(45)

def down_arrow():
    mere.down(50)

onkey(up_arrow, "Up")
onkey(left_arrow, "Left")
onkey(right_arrow, "Right")
onkey(down_arrow, "Down")
onkey(blue, "b")
onkey(green, "g")
onkey(purple, "r")



done()
