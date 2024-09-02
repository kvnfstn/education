import turtle 

def draw_side(l, complete=False):
    if complete:
        turtle.forward(3*l)
    else:
        turtle.forward(l)
        #fractal(l)
        turtle.penup()
        turtle.forward(l)
        turtle.pendown()
        turtle.forward(l)



def fractal(length):
    length = length/3
    termination_clause = length <= 1
    pre_termination_clause = length <= 3
    num_cote = 2 if pre_termination_clause else 3

    if termination_clause:
        return

    turtle.left(60)

    for i in range(num_cote): 
        draw_side(length, pre_termination_clause)
        turtle.right(120)
    
    turtle.forward(length)
    fractal(length)

turtle.pensize(1)
length = 3**5

fractal(length)

turtle.done()
