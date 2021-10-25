import turtle

white = "#fffafa" ;# snow
blue  = "#003b6f" ;# tardis blue
grey  = "#808080"

t=turtle.Pen()
t.speed(10)

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

def chev3x3(color,x,y):
    for xx in(0,1,2):
        for yy in (0,1,2):
            chevron(color,x+xx*-10,y+yy*-10)
    
turtle.bgcolor("black")
chevron(white,0,100)
chevron(white,0,90)
for x in range(-3,4):
    chevron(blue,x*10,80)
for x in range(-4,5):
    chevron(grey,x*10,70)
    chevron(blue,x*10,10)
    chevron(blue,x*10,-30)
    chevron(blue,x*10,-70)
for x in range(-5,6):
    for y in (6,5,-11,-12):
       chevron(blue,x*10,y*10)
for x in (-4,0,4):
    for y in (4,3,2,0,-1,-2,-4,-5,-6,-8,-9,-10):
       chevron(blue,x*10,y*10)
chev3x3(white,-30,40)
chev3x3(white,10,40)

#chevron("black",30,1c0)

turtle.mainloop()