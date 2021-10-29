import random


def placingNumbers(arr, y, x, n):
	if (x == 0): #if mine is at the left-most part of map
		if (arr[y][x+1] != 'X'): arr[y][x+1] += 1
		if (y == 0):
			if (arr[y+1][x] != 'X'): arr[y+1][x] += 1
			if (arr[y+1][x+1] != 'X'): arr[y+1][x+1] += 1
		elif (y>=1 and y<n-1):
			if (arr[y-1][x] != 'X'): arr[y-1][x] += 1
			if (arr[y-1][x+1] != 'X'): arr[y-1][x+1] += 1
			if (arr[y+1][x] != 'X'): arr[y+1][x] += 1
			if (arr[y+1][x+1] != 'X'): arr[y+1][x+1] += 1
		else:
			if (arr[y-1][x] != 'X'): arr[y-1][x] += 1
			if (arr[y-1][x+1] != 'X'): arr[y-1][x+1] += 1

	if (x>=1 and x<n-1):  #if mine is somewhere in the middle of board
		if (arr[y][x-1] != 'X'): arr[y][x-1] += 1
		if (arr[y][x+1] != 'X'): arr[y][x+1] += 1
		if (y == 0): 		  #this is to ascertain where to place the '1' (checks the y-coord)
			if (arr[y+1][x] != 'X'): arr[y+1][x] += 1
			if (arr[y+1][x+1] != 'X'): arr[y+1][x+1] += 1
			if (arr[y+1][x-1] != 'X'): arr[y+1][x-1] += 1
		elif (y>=1 and y<n-1):
			if (arr[y-1][x] != 'X'): arr[y-1][x] += 1
			if (arr[y-1][x+1] != 'X'): arr[y-1][x+1] += 1
			if (arr[y-1][x-1] != 'X'): arr[y-1][x-1] += 1
			if (arr[y+1][x] != 'X'): arr[y+1][x] += 1
			if (arr[y+1][x+1] != 'X'): arr[y+1][x+1] += 1
			if (arr[y+1][x-1] != 'X'): arr[y+1][x-1] += 1

		else:
			if (arr[y-1][x] != 'X'): arr[y-1][x] += 1
			if (arr[y-1][x+1] != 'X'): arr[y-1][x+1] += 1
			if (arr[y-1][x-1] != 'X'): arr[y-1][x-1] += 1

	if (x == n-1):  #if mine is at the right-most part of map
		if (arr[y][x-1] != 'X'): arr[y][x-1] += 1
		if (y == 0):
			if (arr[y+1][x] != 'X'): arr[y+1][x] += 1
			if (arr[y+1][x-1] != 'X'): arr[y+1][x-1] += 1
		elif (y>=1 and y<n-1):
			if (arr[y-1][x] != 'X'): arr[y-1][x] += 1
			if (arr[y-1][x-1] != 'X'): arr[y-1][x-1] += 1
			if (arr[y+1][x] != 'X'): arr[y+1][x] += 1
			if (arr[y+1][x-1] != 'X'): arr[y+1][x-1] += 1
		else:
			if (arr[y-1][x] != 'X'): arr[y-1][x] += 1
			if (arr[y-1][x-1] != 'X'): arr[y-1][x-1] += 1


def mineSweeperBoard(n):		#creating the board
	arr = [[0 for row in range(n)] for column in range(n)] #creates 2d array for the board

	for index in range(2):
		x = random.randint(0, n-1)
		y = random.randint(0, n-1)
		if (arr[y][x] == 'X'):
			index -= 1
		else:
			arr[y][x] = 'X'

			placingNumbers(arr, y, x, n)

	for row in arr: #creates the minesweeper board
		print(" ".join(str(cell) for cell in row)) #puts a space between each zeros
		#print()




if __name__ == "__main__": #serves as the main function
	mineSweeperBoard(7)




