import turtle 

colors = ['red', 'green', 'blue']

for i, c in enumerate(colors):
    turtle.pen(pencolor=c)
    turtle.pensize(i*4+1)
    turtle.forward(100)
    turtle.left(120)
    
turtle.done()
