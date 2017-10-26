from turtle import *

import math
radius=int(input("What is the radius of the flower? "))
petals=int(input("How many petals do you want? "))
#radius=100
#petals=4

import turtle
bob = turtle.Turtle()
bob.speed(100)
bob.shape("turtle")
bob.color("gold")


def draw_arc(b,r):  
    c = 2*math.pi*r 
    ca = c/(360/60)  
    n = int(ca/3)+1 
    l = ca/n  
    for i in range(n):
        bob.fd(l)
        bob.lt(360/(n*6))

def draw_petal(b,r):
    draw_arc(b,r)
    b.lt(180-60)
    draw_arc(b,r)


#draw_petal(bob,radius)

for i in range(petals):
    draw_petal(bob,radius)
    bob.lt(360/petals)

bob.clear()

screen = turtle.Screen()
screen.bgcolor("light sky blue")

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
mere.color(0, 250, 154)
mere.width(5)

def blue():
    mere.color(65, 105, 225)
def green():
    mere.color(50, 205, 50)
def purple():
    mere.color(148, 0, 211)
def yellow():
    mere.color(255, 215, 0)

def up_arrow():
    mere.forward(50)

def left_arrow():
    mere.left(45)

def right_arrow():
    mere.right(45)

def down_arrow():
    mere.back(50)

onkey(up_arrow, "Up")
onkey(left_arrow, "Left")
onkey(right_arrow, "Right")
onkey(down_arrow, "Down")
onkey(blue, "b")
onkey(green, "g")
onkey(purple, "p")
onkey(yellow, "y")
listen()



done()
