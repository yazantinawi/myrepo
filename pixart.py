import turtle
import turtle as t
pixel_size = 30
rows = 20
columns = 20
t.speed(9999)

def init():
    #t.width(5)
    #t.forward(300)
    #t.right(180)
    #t.forward(600)
    #t.right(180)
    #t.forward(300)
    #t.right(90)
    #t.forward(300)
    #t.right(180)
    #t.forward(600)
    #t.right(90)
    #t.width(0)
    t.penup()
    t.setpos(-300,300)
    t.pendown()

def square():
    line = 0
    box = 0
    row = 0
    y = 300

    while line != 4:

        t.forward(pixel_size)
        t.right(90)
        line = line + 1
        if line == 4:
            box = box + 1
            t.forward(pixel_size)
            line = 0
            if box == 20:
                box = 0
                row = row + 1
                turtle.penup()
                y = y - 30
                turtle.setpos(-300 , y)
                turtle.pendown()
                if row == 20:
                    turtle.penup()
                    t.done()

turtle.tracer(0,0)







