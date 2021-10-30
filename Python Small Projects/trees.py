import turtle

def tree(length, level, my_turtle):
	my_turtle.pd()
	#the upper levels are green
	if level > 3:
		my_turtle.color('green')
	else:
		my_turtle.color('brown')

	if length < 10:
		return
	else:
		my_turtle.forward(length)
		my_turtle.right(20)
		tree(length - 20, level + 1, my_turtle)
		#we rotate to the left by twice the angle
		#in order to make the figure symmetric
		my_turtle.left(40)
		tree(length - 20, level + 1, my_turtle)
		#go back to the original orientation
		my_turtle.right(20)
		my_turtle.pu()
		my_turtle.backward(length)

def main():
	wn = turtle.Screen()
	t = turtle.Turtle()
	t.pu()
	t.left(90)
	t.backward(250)
	t.pd()
	t.width(5)
	t.color('brown')
	tree(150, 0, t)
	wn.bgcolor("cyan")

	wn.exitonclick()

main()



