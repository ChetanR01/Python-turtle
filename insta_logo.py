"""
Developed by Chetan Rathod
Youtube Channel link
https://www.youtube.com/channel/UCJ_QxI3rnrC04K0SzvIJvlg
"""

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("white")
t.pensize(20)
t.speed(0)
s.bgpic("ig1.gif")


def get_position():
    t.backward(120)
    t.left(90)
    t.forward(150)
    t.right(90)
    t.clear()


def curve():
    for i in range(90):
        t.right(1)
        t.forward(1)

def border():
    for i in range(4):
        t.forward(200)
        curve()

def startpt():
    t.right(75)
    t.penup()
    t.forward(175)
    t.pendown()

def dot():
    t.right(108)
    t.penup()
    t.forward(30)
    t.right(90)
    t.forward(110) 
    t.right(90)
    t.forward(170)
    t.pendown()

def pause():
    t.speed(1)
    for i in range(150):
        t.right(90)
    

if __name__=="__main__":
    get_position()
    border()
    startpt()
    t.pensize(20)
    t.pencolor("white")
    t.circle(50)
    dot()
    t.pencolor("white")
    t.dot(40)
    pause()
