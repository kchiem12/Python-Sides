
def main():
	#open the file. "r" means read
	dictionary = open("engDictionary.txt", "r")
	real_worlds = [line.strip() for line in dictionary.readLine()]

main()