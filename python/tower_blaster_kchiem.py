import random


def make_tower(length): #for making the initial towers
    tower = []
    for block in range(length): 
        tower.append(random.randint(1,50)) #add blocks from 1 to 50
    return tower

def select_piece(not_used_piece): #this function asks for input what piece the user wants (the parameter is the piece that the computer did not want)
    mystery_piece = random.randint(1, 50) #initalizes mystery piece
    user_select = input("What piece will you choose: " + str(not_used_piece) + " or the mystery piece (enter 'd' for displayed piece, or 'm' for mystery)?\n")
    while (user_select != 'd' and user_select != 'm'): #ensures user input is valid
        user_select = input("Apologies, but you entered an invalid value. Please select again.\n")
    if (user_select == 'd'):  #checks if user selected the displayed block (the user should input 'd')
        return [not_used_piece]
    print("The mystery piece is " + str(mystery_piece))
    use_mystery_piece = input("Do you want to use the mystery piece (type 'y' for yes, or 'n' for no)?\n")
    while (use_mystery_piece != 'y' and use_mystery_piece != 'n'):  #ensures user entered something valid
        use_mystery_piece = input("Please enter a valid input\n")
    if use_mystery_piece == 'y':
        return [mystery_piece]
    return [False, mystery_piece] #if the user does not want mystery piece

def insert_piece(tower, piece): #insert piece into tower at a location which we prompt them to input - make this method return the piece that gets replaced since that piece needs to get sent over to the other player
    location = input("Where would you like to input " + str(piece) + "? Remember, your tower is " + str(len(tower)) + " long so you can choose from 0 to " + str(len(tower)-1) + ":\n") #prompt the user to choose where to input the piece
    while not location.isdigit() or not 0<=int(location)<len(tower):
        location = input("Please make sure to type an integer from 0 to " + str(len(tower)-1) + ":\n")
    replaced = tower[int(location)] #the piece that is getting replaced
    tower[int(location)] = piece #replace the piece
    return replaced #return the piece so we can pass it to the other team

def winning(tower): #check if the tower is in a winning position (if it is in order) 
    for index in range(len(tower)-1): #goes through all but the last block
        if tower[index]>tower[index+1]: #if the block is greater than the next block (out of order), return false
            return False 
    return True #if none of them were out of order, return true
        

def computer_move(tower, piece): #make the computer move 
       #computer splits the tower into two sections
    if piece <= 25: #checks if to see if the piece can fit in the top section
        for loc in range(0, 5): #iterates through the section
            if piece != 25 and piece < tower[loc]: #checks each value if it is greater or less than the piece (if 25, skip entirely)
                replaced = tower[loc]
                tower[loc] = piece
                return replaced #returns the replaced block for next team
            if loc == 4: #if function gets through all values wihout replacing, then replace piece at bottom
                replaced = tower[loc]
                tower[loc] = piece
                return replaced
    else: #in case the piece is greater than 25, goes through the same process as above but at the bottom of the tower
        for loc in range(5, 10): #iterates through the bottom section
            if piece != 50 and piece < tower[loc] or tower[loc] <= 25: #checks if the piece is less than a value in the section
                replaced = tower[loc] #thx
                tower[loc] = piece
                return replaced #returns the replaced block for next team
            if loc == 9:
                replaced = tower[loc]
                tower[loc] = piece #same idea as above (replaces bottom piece if the piece cannot replace any other piece)
                return replaced
    

def main():
    player_tower = make_tower(10) #10 is the length from the flash game
    computer_tower = make_tower(10)
    print("Your tower:", player_tower)
    print("Enemy Tower:", computer_tower)
    available_piece = random.randint(1,50) #setting up the available piece
    is_game_over = False #use this variable to check if the game is over
    while not is_game_over: #while the game is still going on
    
        the_piece = select_piece(available_piece) 
        if the_piece[0] != False:   #this is to check if the player did not choose to forgo the mystery piece
            available_piece = insert_piece(player_tower, the_piece[0]) #sets the available piece to the piece we replace
        else:
            available_piece = the_piece[1]
        print("Your tower:",player_tower)
        
        if winning(player_tower): #if the player wins
            print("You won!") #congratulate them
            print("Computer Tower:", computer_tower)
            is_game_over = True #end the game
               
        else:
            print("Computer is making a move with " + str(available_piece) + "...")
            available_piece = computer_move(computer_tower, available_piece) #set the available piece to the computer's replaced piece
       
            if winning(computer_tower): #if the computer wins
                print("You Lost :(") #notify them
                print("Computer Tower:", computer_tower)
                is_game_over = True #end the game
main()