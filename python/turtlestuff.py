 import turtle 
 
wn = turtle.Screen()

#create a turtle
turtle = turtle.Turtle()
#make the turtle look like a turtle..
turtle.shape("turtle")
turtle.goto(50, 50)
turtle.goto(50, 100)
turtle.goto(100, 100)
turtle.goto(300, 100)
#lift the pen up
#pu stands for pen up
turtle.pu()
turtle.goto(100, 75)
turtle.pd()
turtle.pencolor("green")
turtle.circle(25)
wn.bgcolor("cyan")

wn.exitonclick()

# https://docs.python.org/3.3/library/turtle.html?highlight=turtle

#students now draw something by themselves