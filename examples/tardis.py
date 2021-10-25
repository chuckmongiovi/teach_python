import turtle

white = "#fffafa" ;# snow
blue  = "#003b6f" ;# tardis blue
grey  = "#808080"
red   = "#ff0000"

turtle.speed(0)
turtle.delay(0)

t=turtle.Pen()
def chevron(color,x,y):
    t.hideturtle()
    t.penup()
    t.color(color)
    t.pensize(2)

    t.setpos(x,y)
    t.setheading(120)
    t.forward(1)
    t.pendown()
    t.forward(7)
    t.penup()

    t.setpos(x,y)
    t.setheading(60)
    t.forward(1)
    t.pendown()
    t.forward(7)
    t.penup()

turtle.bgcolor("black")

chevron(white,0,100)
chevron(white,0,90)

for x in range(-3,4):
    chevron(blue,x*10,80)
for x in range(-4,5):
    for y in (7,1,-3,-8):
        if y == 7:
            chevron(grey,x*10,y*10)
        else:
            chevron(blue,x*10,y*10)
for x in range(-5,6):
    for y in (6,5,-13,-14):
       chevron(blue,x*10,y*10)
for x in (-4,0,4):
    for y in (4,3,2,0,-1,-2,-4,-5,-6,-7,-9,-10,-11,-12):
       chevron(blue,x*10,y*10)
for x in (-3,-2,-1,1,2,3):
    for y in (4,3,2):
       chevron(white,x*10,y*10)
for x in (-3,-2,-1):
    for y in (0,-1,-2):
       chevron(white,x*10,y*10)

#chev3x3(white,-30,40)

#chev3x3(white,10,40)
#chev3x3(white,-30,10)

#chev3x3(white,10,40)

turtle.mainloop()