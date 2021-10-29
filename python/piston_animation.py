from drawingpanel import *

height = 750
width = 750
panel = DrawingPanel(width, height)
canvas = panel.canvas

class Sticky_Ball():
	#creates a ball
	def __init__(self, color, posx, posy, vx, vy, radius):
		self.color = color
		self.posx = posx
		self.posy = posy
		self.vx = vx
		self.vy = vy
		self.radius = radius

	def draw(self):
		canvas.create_oval(self.posx - self.radius,
			self.posy - self.radius, 
			self.posx + self.radius,
			self.posy + self.radius, fill=self.color)

	def movement(self):
		self.posx += self.vx
		self.posy += self.vy
		self.vy += 5


		if self.posy + self.radius >= 750:
			self.vy = -self.vy + 20 #so that ball comes up lower and lower each time it bounces


	def movement_1d(self): #called only when the ball is being pushed by piston
		self.posx += self.vx


class Piston():
	#the center is the bottom right of piston
	def __init__(self, posx, posy, length_square):
		self.posx_square = posx
		self.posy_square = posy
		self.len_s = length_square
		self.posx_arm = posx + length_square
		self.posx_arm_moving = self.posx_arm
		self.posx_rect = self.posx_arm_moving + 20

	def draw(self):
		canvas.create_rectangle(self.posx_square, self.posy_square, self.posx_square + self.len_s, self.posy_square - self.len_s, fill = 'gray')
		canvas.create_rectangle(self.posx_arm, self.posy_square - (self.len_s // 4), self.posx_arm_moving + 20, self.posy_square - (self.len_s - self.len_s // 4), fill = '#a78600')
		canvas.create_rectangle(self.posx_rect, self.posy_square, self.posx_rect + 10, self.posy_square - self.len_s, fill = '#a78600')

	def movement(self, velocity):
		self.posx_arm_moving += velocity
		self.posx_rect += velocity


def main():
	piston = Piston(0, 200, 100)
	ball1 = Sticky_Ball("red", 180, 150, 15, 20, 30)
	hit = False

	while 1:
		piston.draw()

		panel.sleep(1)
		panel.clear()

		if piston.posx_arm_moving < 200:
			piston.movement(ball1.vx)

		ball1.draw()
		if ball1.posx - ball1.radius <= piston.posx_rect + 10:
			hit = True

		if hit and ball1.posx - ball1.radius <= piston.posx_rect + 10:
			ball1.movement_1d()
		elif hit:
			ball1.movement()
		ball1.draw()
		piston.draw()

	panel.mainloop()


main()

