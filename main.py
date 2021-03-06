import turtle


"""
i know its long but it looks nice i guess 

mustafa - period 6
"""

# this just sets up the the flower and location
turtle.penup()
turtle.left(90)
turtle.fd(200)
turtle.pendown()
turtle.right(90)

# the color of flower can be set with starting function
def base(color):
    turtle.fillcolor (color)
    turtle.begin_fill ()
    # this sets the color of the flower based on what you choose
    turtle.circle (10,180)
    turtle.circle (25,110)
    turtle.left (50)
    turtle.circle (60,45)
    turtle.circle (20,170)
    turtle.right (24)
    turtle.fd (30)
    turtle.left (10)
    turtle.circle (30,110)
    turtle.fd (20)
    turtle.left (40)
    turtle.circle (90,70)
    turtle.circle (30,150)
    turtle.right (30)
    turtle.fd (15)
    turtle.circle (80,90)
    turtle.left (15)
    turtle.fd (45)
    turtle.right (165)
    turtle.fd (20)
    turtle.left (155)
    turtle.circle (150,80)
    turtle.left (50)
    turtle.circle (150,90)
    turtle.end_fill ()
    # this ends the flower 

# draws the petals on the flower based on location of flower
def petals():
    turtle.left (150)
    turtle.circle (-90,70)
    turtle.left (20)
    turtle.circle (75,105)
    turtle.setheading (60)
    turtle.circle (80,98)
    turtle.circle (-90,40)
    turtle.left (180)
    turtle.circle (90,40)
    turtle.circle (-80,98)
    turtle.setheading (-83)

# draws a leave on the flower 
def leaves():
    turtle.fd (30)
    turtle.left (90)
    turtle.fd (25)
    turtle.left (45)
    turtle.fillcolor ("darkgreen")
    turtle.begin_fill ()
    turtle.circle (-80,90)
    turtle.right (90)
    turtle.circle (-80,90)
    turtle.end_fill ()
    turtle.right (135)
    turtle.fd (60)
    turtle.left (180)
    turtle.fd (85)
    turtle.left (90)
    turtle.fd (80)

# set the color of the flower
base("red")
# calls the petal and leaves function
petals()
leaves()
# so the project doesnt die when it completes
turtle.done()