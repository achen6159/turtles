import math
radius=int(input("What is the radius of the flower? "))
petals=int(input("How many petals do you want? "))
#radius=100
#petals=4

import turtle
bob = turtle.Turtle()
bob.speed(100)
bob.shape("turtle")
bob.color("medium sea green")


def draw_arc(b,r):  
    bob.speed(100)
    c = 2*math.pi*r 
    ca = c/(360/60)  
    n = int(ca/3)+1 
    l = ca/n  
    for i in range(n):
        bob.fd(l)
        bob.lt(360/(n*6))

def draw_petal(b,r):
    bob.speed(100)
    draw_arc(b,r)
    b.lt(180-60)
    draw_arc(b,r)


#draw_petal(bob,radius)

for i in range(petals):
    draw_petal(bob,radius)
    bob.lt(360/petals)


turtle.done()



