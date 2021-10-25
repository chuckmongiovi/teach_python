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

def star8(color,x,y):
    t.hideturtle()
    t.penup()
    t.color(color)
    t.pensize(2)

    t.setpos(x+5,y)
    t.setheading(315)
    t.pendown()
    t.forward(20)
    t.penup()
    
turtle.bgcolor("black")

chevron(white,0,100)
chevron(white,0,90)

star8(red,10,0)
star8(red,50,0)

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

for xx in (-3,1):
    for yy in (-4,-9):
        for x in (0,1,2):
            chevron(grey,(xx+x)*10,yy*10)
            chevron(grey,(xx+x)*10,(yy-3)*10)
            if x == 1:
                color = blue
            else:
                color = grey
            chevron(color,(xx+x)*10,(yy-1)*10)
            chevron(color,(xx+x)*10,(yy-2)*10)

turtle.mainloop()