import random

def print_intro():
	'''Prints out the intro and directions for the Hammurabi game'''
	print("""Congrats, you are the newest ruler of ancient Samaria, elected for a ten year term
of office. Your duties are to distribute food, direct farming, and buy and sell land
as needed to support your people. Watch out for rat infestations and the resultant
plague! Grain is the general currency, measured in bushels. The following will help
you in your decisions:

(a) Each person needs at least 20 bushels of grain per year to survive.
(b) Each person can farm at most 10 acres of land.
(c) It takes 2 bushels of grain to farm an acre of land.
(d) The market price for land fluctuates yearly.

Rule wisely and you will be showered with appreciation at the end of your term. Rule
poorly and you will be kicked out of office!
""")

# where the magic begins
def Hammurabi():
	starved = 0
	immigrants = 5
	population = 100
	harvest = 3000 # total bushels harvested
	bushels_per_acre = 3 # amount harvested for each acre planted
	rats_ate = 200 # bushels destroyed by rats
	bushels_in_storage = 2800
	acres_owned = 1000
	cost_per_acre = 19 # each acre costs this many bushels
	plague_deaths = 0

	total_starved = 0  # Keeps tally of total amount starved for the final summary

	print_intro()

	for year in range(1, 11):
		print("O great Hammurabi!")
		print("You are in year " + str(year) + " of your ten year rule.")
		print("In the previous year " + str(starved) + " people starved to death.")
		print("In the previous year " + str(immigrants) + " people entered the kingdom.")
		print("The population is now " + str(population) + ".")
		print("We harvested " + str(harvest) + " bushels at " + str(bushels_per_acre) + " bushels per acre.")
		print("Rats destroyed " + str(rats_ate) + " bushels, leaving " + str(bushels_in_storage) + " bushels in storage.")
		print("The city owns " + str(acres_owned) + " acres of land.")
		print("Land is currently worth " + str(cost_per_acre) + " bushels per acre")
		print("There were " + str(plague_deaths) + " deaths from the plague.")

		# Asks how many acres of land the player wants to purchase
		acres_bought = ask_to_buy_land(bushels_in_storage, cost_per_acre)
		bushels_in_storage = bushels_in_storage - (acres_bought * cost_per_acre)
		acres_owned = acres_owned + acres_bought

		# Asks player how many acres they want to sell if they did not buy any acres before
		if acres_bought == 0:
			acres_sold = ask_to_sell_land(acres_owned)
			acres_owned = acres_owned - acres_sold
			bushels_in_storage = bushels_in_storage + (acres_sold * cost_per_acre)

		# Asks player how many bushels they want to give to their citizens
		amount_fed = ask_to_feed(bushels_in_storage)
		bushels_in_storage = bushels_in_storage - amount_fed

		# Asks player how many acres of land they want to cultivate (two bushels per acre)
		land_cultivated = ask_to_cultivate(acres_owned, population, bushels_in_storage)
		bushels_in_storage = bushels_in_storage - (land_cultivated*2)

		print()

		# Determines whether or not a plague happens.
		# If plague happens, it calculates the amount of people dead and updates the total population
		plague_deaths = 0
		if is_plague():
			plague_deaths = int(population / 2)
			population = population - plague_deaths

		# Determines the amount of people that starved during the year, and determines if more than 45% of population starved to death
		starved = num_starving(population, amount_fed)
		total_starved = total_starved + starved
		if starved >= population * 0.45:
			print("O Hammurabi! 45 percent or more of your entire population starved to death!")
			print("Only a monster could you let this catastrophe ravage his or her fellow citizens!")
			break
		population = population - starved

		# Calculates the amount of immigrants that Samaria receives the next year
		immigrants = num_immigrants(acres_owned, bushels_in_storage, population, starved)
		population = population + immigrants

		# Calculates the per-acre bushel yield
		bushels_per_acre = get_harvest()
		harvest = land_cultivated * bushels_per_acre
		bushels_in_storage = bushels_in_storage + harvest

		# Determines if a rat infestation happens this year
		# If it does happen, then it calculates the percentage of bushels that are destroyed by rats
		if do_rats_infest():
			rats_ate = int(bushels_in_storage*percent_destroyed())
			bushels_in_storage = bushels_in_storage - rats_ate
		else:
			rats_ate = 0

		# Determines the price of an acre of land for the next year
		cost_per_acre = price_of_land()


	# Special message if the user starves 45% of citizens
	if starved >= population * 0.45:
		print("Hammurabi! You have been thrown out of power for inadvertantly slaughtering so many of your people!")
		print("Here is your end-of-term report of the empire:")
		print()
	else:	
		print("O great Hammurabi! Your 10 year term is over! Here is your end-of-term report of the empire:")
		print()

	# End-of-term statistics
	print("A total of " + str(total_starved) + " people starved to death during your reign.")
	print("Your civilization stretches across " + str(acres_owned) + " acres of land.")
	print()

	# End-Of-Term review on how the user did depending on whether or not a person starved to death
	if total_starved > 20:
		print("O Hammurabi, many people starved to death during your tenure!\nYou will be described as a murderer in the history books.")
	elif 0 < total_starved <= 20:
		print("O Hammurabi, some people starved to death during your tenure!\nThis will not bode well for you in terms of your legacy.")
	else:
		print("O great Hammurabi, not one person has starved to death during your tenure!\nYou will be honored and respected by future generations for keeping your citizens well-fed.")

	# End-Of-Term review on how user did depending on if the kingdom of Samaria expanded or shrunk
	if acres_owned < 1000:
		print("Also, the kingdom of Samaria shrank during your tenure!\nThis may be seen by future generations as Samaria losing its wealth and prosperity during your reign!\n")
	elif acres_owned == 1000:
		print("Also, the kingdom of Samaria neither shrank nor grew during your tenure!\nAlthough it is not terrible, you did not make much of an impact in history to make you well-known for generations to come\n")
	elif 1000 < acres_owned < 1100:
		print("Also, the kingdom of Samaria expanded its territory a bit during your tenure!\nA fine job great Hammurabi, but probably not enough to leave an indelible mark on history.\n")
	else:
		print("Also, the kingdom of Samaria expanded its territoy by quite a bit during your tenure!\nWhat an impressive feat great Hammurabi! You will surely be recognized for this accomplishment by generations to come!\n")


'''Below are all the functions used in the Hammurabi program'''


def ask_to_buy_land(bushels, cost):
	'''Asks user how many bushels to spend buying land.'''
	acres = int(input("How many acres will you buy? "))
	while acres * cost > bushels:
		print("O great Hammurabi, we only have but " + str(bushels) + " bushels of grain, and thus cannot afford this many acres!")
		acres = int(input("O great Hammurabi, how many acres will you buy? "))
	return acres

def ask_to_sell_land(acres):
	'''Asks user how many acres to sell'''
	amount_to_sell = int(input("How many acres will you sell? "))
	while amount_to_sell > acres:
		print("O great Hammurabi, we only have but " + str(acres) + " acres of land, and thus cannot sell more than that!")
		amount_to_sell = int(input("O great Hammurabi, how many acres will you sell?"))
	return  amount_to_sell

def ask_to_feed(bushels):
	'''Asks user how many bushels to give to citizens'''
	amount_for_feeding = int(input("How many bushels will you bestow upon your citizens? "))
	while amount_for_feeding > bushels:
		print("O great Hammurabi, we only have but " + str(bushels) + " bushels of grain to distribute to our citizens!")
		amount_for_feeding = int(input("O great Hammurabi, how many bushels will you give to your citizens? "))
	return amount_for_feeding

def ask_to_cultivate(acres, population, bushels):
	'''Asks user how much land to plant seeds in'''
	acres_to_cultivate = int(input("How many acres do you want to cultivate with seeds? "))
	the_max = 10 * population
	if the_max > acres:
		the_max = acres
	while acres_to_cultivate > the_max or acres_to_cultivate * 2 > bushels:
		if acres_to_cultivate > the_max and 10 * population >= acres:
			print("O great Hammurabi, we only have but " + str(acres) + " acres of land to cultivate!")
			acres_to_cultivate = int(input("O great Hammurabi, how many acres of land do you want to cultivate with seeds? "))
		elif acres_to_cultivate > the_max and 10 * population < acres:
			print("O great Hammurabi, we only have but " + str(population) + " citizens that can tend to a max of " + str((10 * population)) + " acres of land!")
			acres_to_cultivate = int(input("O great Hammurabi, how many acres of land do you want to cultivate with seeds? "))
		else:
			print("O great Hammurabi, we only have but " + str(bushels) + " bushels of grain, which cannot cultivate all " + str(acres_to_cultivate) + " acres of land!")
			acres_to_cultivate = int(input("O great Hammurabi, how many acres of land do you want to cultivate with seeds? "))
	return acres_to_cultivate

def is_plague():
	'''Determines if there is a plague event during the year'''
	chance = random.randint(1, 100)
	if chance <= 15:
		return True
	return False

def num_starving(population, bushels):
	'''Determines how many people starve to death based on amount of bushels given to feed'''
	bushels_needed_for_everyone = population * 20
	people_starved = 0
	if bushels < bushels_needed_for_everyone:
		people_starved = population - bushels // 20
	return people_starved

def num_immigrants(land, grain_in_storage, population, num_starving):
	'''Calculates the number of immigrants that come in the next year'''
	if num_starving > 0:
		return 0
	immigrants = int((20*land+grain_in_storage) / ((100*population)+1))
	return immigrants

def get_harvest():
	'''Determines the yield of bushels per acre'''
	return random.randint(1, 8)

def do_rats_infest():
	'''Determines if there is a rat infestation during the year'''
	chance = random.randint(1, 100)
	if chance <= 40:
		return True
	return False

def percent_destroyed():
	'''Determines the percentage amount of bushels in the storage destroyed by rats
		(if rat infestation does occur during the year)'''
	destroyed = random.randint(10, 30) / 100
	return destroyed 

def price_of_land():
	'''Determines the price of an acre of land for the next year'''
	return random.randint(16, 22)





def main():
	'''Contains the heart of the code (and why not put the function in the main function)'''
	Hammurabi()

main()
