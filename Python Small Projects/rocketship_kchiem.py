def print_fancybox(n):
	print("----------------")
	if n > 1:
		for x in range (1, n):
			print("|" + "\\/" * 7 + "|")
		for y in range (1, n):
			print("|" + "/\\" * 7 + "|")
	print("----------------")

def print_pyramid(n):
	if n > 0:
		space_counter = n - 1
		print(" " * space_counter, end="")
		space_counter = space_counter - 1
		print("/\\")
		for each_row in range(1, n):
			print(" " * space_counter, end="")
			space_counter = space_counter - 1
			print("/", end="")
			print("*=" * each_row, end="")
			print("\\")
		print("-" * (n*2))

def print_rocketship1():
	cones_rocketship(3)
	separating_rocketship_parts(3)
	rectangle_up(3)
	rectangle_down(3)
	separating_rocketship_parts(3)
	rectangle_down(3)
	rectangle_up(3)
	separating_rocketship_parts(3)
	cones_rocketship(3)

def print_rocketship2(n):
	cones_rocketship(n)
	separating_rocketship_parts(n)
	rectangle_up(n)
	rectangle_down(n)
	separating_rocketship_parts(n)
	rectangle_down(n)
	rectangle_up(n)
	separating_rocketship_parts(n)
	cones_rocketship(n)

def cones_rocketship(x):
	space_counter = x*2-1
	slashes = 1
	for top_cone in range(1, x*2):
		print(" " * space_counter, end="")
		print("/" * slashes, end="")
		print("**", end="")
		print("\\" * slashes, end="")
		slashes = slashes + 1
		space_counter = space_counter - 1
		print()

def separating_rocketship_parts(x):
	print("+", end="")
	for bars in range(x*2):
		print("=*", end="")
	print("+")

def rectangle_up(x):
	amount_of_dots = x-1
	amount_of_arrows = 1
	dots_in_middle = x*2-2
	for each_row in range(x):
		print("|", end="")
		dots_at_ends(amount_of_dots)
		up_arrows(amount_of_arrows)
		print("." * dots_in_middle, end="")
		up_arrows(amount_of_arrows)
		dots_at_ends(amount_of_dots)
		print("|")
		if each_row < x-1:
			amount_of_dots = amount_of_dots - 1
			amount_of_arrows = amount_of_arrows + 1
			dots_in_middle = dots_in_middle - 2

def rectangle_down(x):
	amount_of_dots = 0
	amount_of_arrows = x
	dots_in_middle = 0
	for each_row in range(x):
		print("|", end="")
		dots_at_ends(amount_of_dots)
		down_arrows(amount_of_arrows)
		print("." * dots_in_middle, end="")
		down_arrows(amount_of_arrows)
		dots_at_ends(amount_of_dots)
		print("|")
		if each_row < x-1:
			amount_of_dots = amount_of_dots + 1
			amount_of_arrows = amount_of_arrows - 1
			dots_in_middle = dots_in_middle + 2

def dots_at_ends(y):
	print("." * y, end="")

def up_arrows(y):
	print("/\\" * y, end="")

def down_arrows(y):
	print("\\/" * y, end="")

def main():
	print_fancybox(4)
	print_pyramid(3)
	print_rocketship1()
	print_rocketship2(5)

main()