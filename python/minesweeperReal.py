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


def minesweeperBoard(n, k):		#creating the board
	arr = [[0 for row in range(n)] for column in range(n)] #creates 2d array for the board

	for index in range(k):
		x = random.randint(0, n-1)
		y = random.randint(0, n-1)
		if (arr[y][x] == 'X'):
			index -= 1
		else:
			arr[y][x] = 'X'

			placingNumbers(arr, y, x, n)

	return arr

def playerBoard(n): #constructs the player's map
	arr = [['-' for row in range(n)] for column in range(n)]
	return arr

def displayBoard(board): #displays the board
	for row in board:
		print(" ".join(str(cell) for cell in row))

def checkCondition(board): #check whether person won
	for row in board:
		for cell in row:
			if cell == '-':
				return False
	return True


def clearZeros(playerBoard, hiddenBoard, x, y): #clears all zero spaces around if player hits a tile that is a zero
	length = len(playerBoard)
	theArr = playerBoard
	temp = x
	while temp < length-1:
		if hiddenBoard[temp+1][y] == 0:
			theArr[temp+1][y] = hiddenBoard[temp+1][y]
			temp += 1
		else:
			break
	temp = x
	while temp > 0:
		if hiddenBoard[temp-1][y] == 0:
			theArr[temp-1][y] = hiddenBoard[temp-1][y]
			temp -= 1
		else:
			break
	temp = y
	while temp < length-1:
		if hiddenBoard[x][temp+1] == 0:
			theArr[x][temp+1] = hiddenBoard[x][temp+1]
			temp += 1
		else:
			break
	temp = y
	while temp > 0:
		if hiddenBoard[x][temp-1] == 0:
			theArr[x][temp-1] = hiddenBoard[x][temp-1]
			temp -= 1
		else:
			break




	#if (x != 0):
		#while 

def startOver(n): #allows player the option to start over if they win or lose the game
	if n == 0:
		print("Congratulations! Enter 's' if you want to start again. Otherwise, enter 'n'")
		option = input()
		if option == 's':
			return 0
		else:
			return 1
	else:
		print("That is unfortunate! Enter 's' if you want to start over, otherwise enter 'n'")
		option = input()
		if option == 's':
			return 0
		else:
			return 1

#def flagging(): #option to flag a tile


def LeGame(): #heart of the game
	continueGame = True 

	while continueGame:
		print("Select the difficulty:")
		diff = input("Easy (e), Medium (m), Hard (h)")
		n, k = 0, 0
		while (diff != 'e' and diff != 'm' and diff != 'h'): #ensures valid input
			diff = input("Input a valid letter...")

		if (diff == 'e'):
			n = 8
			k = 10
		elif (diff == 'm'):
			n = 14
			k = 40
		else: 
			n = 20
			k = 99

		theActualBoard = minesweeperBoard(n, k)
		theDisplayBoard = playerBoard(n)

		while True:
			print()
			displayBoard(theDisplayBoard)
			x = int(input("Input the row of the tile you want to select: "))
			y = int(input("Input the column of the tile you want to select: "))
			x-=1 #due to 0 indexing
			y-=1
			theDisplayBoard[x][y] = theActualBoard[x][y]

			if (theDisplayBoard[x][y] == 'X'):
				displayBoard(theActualBoard)
				toStart = startOver(1)
				if toStart == 0:
					break
				else:
					continueGame = False
					break
			else:
				condition = checkCondition(theDisplayBoard)
				if condition == True:
					toStart = startOver(0)
					if toStart == 0:
						break
					else:
						continueGame = False
						break




	





if __name__ == "__main__": #serves as the main function
	try:
		LeGame()
	except KeyboardInterrupt:
		print("\nEnd of Game.")




