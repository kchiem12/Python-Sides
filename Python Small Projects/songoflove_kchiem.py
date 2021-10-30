def firstVerse():
	print("I like you, Fred, I like you!\nYou're just saying those words to be kind.\nNo, I mean it.  I like... I mean I love you, Fred!\nHe is out of his medieval mind!\nI'm perfectly sane and sound!  I never felt better in my life!\nEverybody... everybody, everybody!  Come on!  And meet my incipient wife!\n")

def secondVerse():
	print(firstLine() + "My reasons must be clear.\nWhen she shows you all how strong she is you'll stand right up and cheer!\n" + lastTwoLines())

def thirdVerse():
	print(firstLine() + "She drinks just like a lord!\nSo sing a merry drinking song and let the wine be poured!\n" + lastThreeLines())

def fourthVerse():
	print(firstLine() + "She sings just like a bird!\nYou'll be left completely speechless when her gentle voice is heard!\n" + lastFourLines())

def fifthVerse():
	print(firstLine() + "She wrestles like a Greek!\nYou will clap your hands in wonder at her fabulous technique!\n" + lastFiveLines())

def sixthVerse():
	print(firstLine() + "She dances with such grace!\nYou are bound to sing her praises 'til you're purple in the face!\n" + lastSixLines())

def seventhVerse():
	print(firstLine() + "She's musical to boot!\nShe will set your feet a-tapping when she plays upon her lute!\n" + lastSevenLines())

def eigthVerse():
	print(firstLine() + "A clever, clownish wit!\nWhen she does her funny pantomime your sides are sure to split!\nHa ha ha ha, ho ho ho ho, ha ha ha ha ho!\n" + lastSevenLines())

def lastVerse():
	print("I'm in love with a girl.\nHe's in love with a girl named \"F-R-E-D\" Fred!")

def firstLine():
	return("I'm in love with a girl named Fred.\n")

def lastTwoLines():
	return ("With a \"F\" and a \"R\" and an \"E\" and a \"D\"\nAnd a \"F-R-E-D\" Fred!  Yeah!\n")

def lastThreeLines():
	return ("Fill the bowl to overflowing.  Raise the goblet high!\n" + lastTwoLines())

def lastFourLines():
	return ("La la la la, la la la la, la la la la la!\n" + lastThreeLines())

def lastFiveLines():
	return ("Clap clap, clap clap, clap clap clap clap, clap, clap clap!\n" + lastFourLines())

def lastSixLines():
	return ("Bravo!  Bravo!  Bravissimo bravo!  Bravissimo!\n" + lastFiveLines())

def lastSevenLines():
	return ("Strum strum, strum strum, strum strum strum strum strum, strum.\n" + lastSixLines())

def main():
	firstVerse()
	secondVerse()
	thirdVerse()
	fourthVerse()
	fifthVerse()
	sixthVerse()
	seventhVerse()
	eigthVerse()
	lastVerse()

main()