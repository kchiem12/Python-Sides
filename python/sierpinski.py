from drawingpanel import *

width = 1024
height = 768
panel = DrawingPanel(width, height)
canvas = panel.canvas


def draw_triangle(n, x, y, size):
	canvas = panel.canvas
	points = [x - size / 2, y + size / 2, x, y - size / 2, x + size / 2, y + size / 2]
	if n == 0:
		canvas.create_polygon(points, outline = 'black', fill = 'blue') #used the create_polygon function to color in triangle
	else: 
		canvas.create_polygon(points, outline = 'black', fill = 'yellow')


def sierpinski(n, x, y, size):

	#draw main triangle
	draw_triangle(n, x, y, size)

	if n == 0:
		return

	x0 = x - size / 4
	y0 = y + size / 4
	x1 = x + size / 4
	y1 = y + size / 4
	x2 = x
	y2 = y - size / 4

	sierpinski(n - 1, x0, y0, size / 2)
	sierpinski(n - 1, x1, y1, size / 2)
	sierpinski(n - 1, x2, y2, size / 2)



sierpinski(7, width / 2, height / 2, width / 2)
