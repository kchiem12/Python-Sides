def mystery(x):
	mine = ""
	for c in x:
		mine = c + mine
	return mine

def main():
	print(mystery("bruh"))

main()