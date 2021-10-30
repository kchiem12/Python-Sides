from drawingpanel import *

height = 500
width = 500
panel  = DrawingPanel(width, height)
panel.set_background("white")
canvas = panel.canvas

class Ball():
	def __init__(self, ball_color, positionx, positiony, radius, vx, vy):
		self.color = ball_color #make the color for this ball = ball_color
		self.positionx= positionx
		self.positiony = positiony
		self.radius = radius
		self.vx = vx
		self.vy = vy

	def update(self):
		self.positionx += self.vx
		self.vy += 5
		self.positiony += self.vy


		#bounce off walls
		


		# if self.positionx >= 400:
		# 	self.vx = -self.vx
		if self.positiony >= 400:
		 	self.vy = -self.vy

	def draw(self):
		canvas.create_oval(self.positionx - self.radius, 
			self.positiony - self.radius
			, self.positionx + self.radius, 
			self.positiony + self.radius, fill = self.color)

def main():
	#ball_color, positionx, positiony, radius, vx, vy
	ball = Ball("red", 100, 100, 5, 25, 5)
	

	while 1:
		ball.draw()
		panel.sleep(50)
		#erase everything
		panel.clear()

		
		ball.update()
		ball.draw()

  #need this for drawing panel to work
	panel.mainloop()

main()


