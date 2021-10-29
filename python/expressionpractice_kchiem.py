#gets first letter of name
def whatName(name):
	return name[0]

#calculates current age (assuming the month of birth is july or earlier)
def ageCalculator(yearOfBirth):
	return str((2020 - yearOfBirth))

#gets one solution
def quadraticFormula1(a, b, c):
	return str(((-b) + (b**2 - 4*a*c)**0.5) / (2*a))

#gets one solution
def quadraticFormula2(a, b, c):
	return str(((-b) - (b**2 - 4*a*c)**0.5) / (2*a))

def main():
	theName = input("What's your name? ")
	print("Your name begins with " + whatName(theName))
	theYear = input("When were you born? ")
	print("You are " + ageCalculator(int(theYear)))
	print("Let's solve a quadratic equation")
	theA = input("What is the coefficient of x^2? ")
	theB = input("What is the coefficient of x? ")
	theC = input("What is the constant term? ")
	print("One solution for the quadratic is " + quadraticFormula1(int(theA), int(theB), int(theC)))
	print("The other solution for the quadratic is " + quadraticFormula2(int(theA), int(theB), int(theC)))

main()