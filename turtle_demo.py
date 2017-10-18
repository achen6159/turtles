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
    
anders.speed(100)
draw_star(anders, 50, 0, 36, "medium violet red", "DarkOrchid1")
annie.speed(100)
draw_star(annie, 0, 0, 36, "peach puff", "DodgerBlue2")
saleem.speed(100)
draw_star(saleem, -50, 0, 36, "CadetBlue2", "medium sea green")
nathan.speed(100)            
draw_star(nathan, -100, 0, 36, "DeepSkyBlue3", "gold")
annie.speed(100)
draw_star(annie, -150, 0, 36, "lawn green", "orange red")
saleem.speed(100)
draw_star(saleem, -200, 0, 36, "dark turquoise", "firebrick1")



done()
