#import TKinter;

import turtle;

t = turtle.Pen();
t.hideturtle();
t.speed(0);

for x in range(100):
    t.forward(x)
    t.left(90)

turtle.mainloop()