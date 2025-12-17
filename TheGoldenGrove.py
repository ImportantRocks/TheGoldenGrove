import random
import string
import pickle
import os
from time import sleep
#Chloe Gaechter - 04/05/2021

#Defining global variables
wormCount = 0
fishCount = 0
location = [
    'A small stream nearby',
    'Kinley Lake']
day = 1
playerName = ''


#Saving and loading functionality-----------------
#set the variable that points to the correct file
#if the file is not found, it will create one
save1 = "saveGame1.txt"

def saveGame():

    #Open the file in 'Write Binary' mode
    outfile = open(save1,'wb')

    #"Dump" puts the requested information into the file in binary format (Serializes it)
    #It takes in all variables you want to save as one object, then it takes the file you want to save the variables to (outfile)
    pickle.dump([wormCount, fishCount, location, day, playerName], outfile)

    #Close the file when it's done
    outfile.close()
    
    #Call the start function to return to the game
    start()

def loadGame():

    #Open the file in 'Read Binary' mode
    infile = open(save1,'rb')


    #Take in each variable in order as a new variable with the same name to keep track
    new_wormCount, new_fishCount, new_location, new_day, new_playerName = pickle.load(infile)

    #Close the file now that we have the data back
    infile.close()

    #Get the global variables we want to update
    global wormCount
    global fishCount
    global location
    global day
    global playerName

    #set the global variables to the values of the "new_" vairables
    wormCount = new_wormCount
    fishCount = new_fishCount
    location = new_location
    day = new_day
    playerName = new_playerName

    #Call the start function to return to the game
    start()


#The main camp
def start():
    print(f"--- Day: {day} ---")

    print(f"What would you like to do today, {playerName}?")
    print("1. Go to your tent")
    print("2. Check your tackle")
    print("3. Enter the cave")
    print("4. Go fishin'")
    print("S. Save Game")

    selection = input("Selection: ")
    if selection == "1":
        print('')
        tent()
    if selection == "2":
        print('')
        tackle()
    if selection == "3":
        print('')
        cave()
    if selection == "4":
        print('')
        fishing()
    if selection == "s":
        print('')
        saveGame()


#4. Fishing --------------------------------------
def fishing():

    global fishCount
    global wormCount
    global location
    global day
    catchScore = 0

    if wormCount <= 0:
        print("You don't have any bait, but you can still go out on a hike if you would like?")
        print("1. Go on a hike")
        print("e. Go back to your camp")
        selection = input("Selection: ")
        if selection == "e":
            locationChoice = 0
            print('')
            start()
        if selection == "1":
            print('')
            hike()
            day += 1
            

    
    elif wormCount > 0:
        #Select where you want to go fishing
        print("Where do you want to go fishing today?")
        print("1. The small stream nearby")
        print("2. Kinley Lake")

        selection = input("Selection: ")
        if selection == "1":
            locationChoice = 0
            print('')
        if selection == "2":
            locationChoice = 1
            print('')

        #start of minigame
        day += 1

        print(f"With your tackle box and fishing pole, you head down to {location[locationChoice]}.")
        print("")
        sleep(3)

        castScore = random.randrange(0,10)
        if castScore <= 2:
            print("Your cast goes wide")
        if 2 < castScore < 8:
            print("You cast your line into the water") 
        if castScore >=8:
            print("You make a great cast into the perfect spot")
        if castScore == 10:
            print("You make a great cast into the perfect spot")
            print("")
            sleep(3)
            print("You really nailed it with that one!")
        print("")
        sleep(3)

        baitScore = random.randrange(0,10)
        if baitScore <= 2:
            print("Your bait is not very inticing to the fish")
        if 2 < baitScore < 8:
            print("Your bait is wiggling around")
        if baitScore >= 8:
            print("Your bait is doing great work")
        if baitScore == 10:
            print("Your bait is doing great work")
            print("")
            sleep(3)
            print("Wow, it's really putting on a show!")
        print("")
        sleep(3)

        print("After feeling a few nibbles, a fish bites your hook!")
        print("")
        sleep(3)

        reelScore = random.randrange(0,10)
        if reelScore <= 2:
            print("Your line gets tangled as you reel in the fish!")
        if 2 < reelScore < 8:
            print("You reel in the fish steadily")
        if reelScore >= 8:
            print("You reel in the fish close to the shore")
        if reelScore == 10:
            print("You reel in the fish with ease")
            print("")
            sleep(3)
            print("The fish stood no chance!")
        print("")
        sleep(3)

        catchScore = castScore + baitScore + reelScore

        if catchScore >= 8:

            wormCount -= 1
            fishCount += 1

            print("You reel in the fish and scoop it into your net.")
            print("")
            sleep(3)

            print("e: Take your fish back to camp")

            selection = input("Selection: ")
            if selection == "e":
                print('')
                castScore, baitScore, setScore, reelScore = 0,0,0,0
                start()

        if catchScore < 8:
            wormCount -= 1

            print("Your line goes loose as you watch the fish swim away.")
            print("")
            sleep(2)
            print("You lost the fish.")
            print("")
            sleep(2)

            print("e: Head back to camp empty handed.")

            selection = input("Selection: ")
            if selection == "e":
                print('')
                castScore, baitScore, setScore, reelScore = 0,0,0,0
                start()

def hike():

    global day

    print("Where would you like to go hiking?")
    print("1. The small stream nearby")
    print("2. Kinley Lake")

    selection = input("Selection: ")
    if selection == "1":
        day += 1
        print('')
        print('You take a long walk down the current of the stream, taking note of all the many creatures singing their songs')
        print('')
        sleep(5)
        print("""You lay back and listen as the song transforms from birds and bugs to the croaks of frogs and chirps 
    of crickets. It's time to head home now.""")
        print('')
        sleep(5)
        start()
    if selection == "2":
        day += 1
        print('')
        print('You make your way to your regular fishing spot at Kinley Lake. The soft waves of the water against the shoreline is very soothing.')
        print('')
        sleep(5)
        print("After you spend some time gazing at the lake, you head home.")
        print('')
        sleep(5)
        start()


#3. Cave -----------------------------------------
def cave():
    print("You enter the small cave opening and find a circular room with a dirt floor. On the other side of the room there is a crack forming in the cave wall.")
    print("1. Collect worms from the cave floor")
    print("e: Exit the cave")

    selection = input("Selection: ")
    if selection == "1":
        print('')
        worms()
    if selection == "e":
        print('')
        start()

def worms():
    newWorms = random.randrange(1,5)
    print(f"You wander the room flipping over rocks and find {newWorms} worms.")
    global wormCount
    wormCount += newWorms
    print("1. Collect more worms")
    print("e: Exit the cave")

    selection = input("Selection: ")
    if selection == "e":
        print('')
        start()
    if selection == "1":
        print('')
        worms()


#2. Tackle ---------------------------------------
def tackle():
    print("You open up your tackle box and check the state of your equipment.")
    print('---------------------')
    print(f"Bait: {wormCount}")  
    print('---------------------')
    print("e: Exit to camp")

    selection = input("Selection: ")
    if selection == "1":
        print('')
    if selection == "e":
        print('')
        start()


#1. Tent -----------------------------------------
def tent():
    print("You enter the tent and see a sleeping bag on the ground and a desk with a small journal.")

    print("1: Look at the journal")
    print("2. Go to sleep")
    print("e: Exit the tent")

    selection = input("Selection: ")
    if selection == "1":
        print('')
        journal()
    if selection == "2":
        print('')
        slumber()
    if selection == "e":
        print('')
        start()
        
def journal():
    print("you pick up the journal and flip through a few of the pages. It is a record of all the fish you've caught.")
    print('---------')

    if fishCount == 0:
        print("You haven't caught any fish yet")
    if fishCount > 0:
        print(f'You have caught {fishCount} fish')

    print('---------')


    print("e: Exit journal")

    selection = input("Selection: ")
    if selection == "e":
        print('')
        tent()

def slumber():

    global day

    print("You get into your bed and drift off to sleep")
    print("")
    for i in range(3):
        print(". ")
        sleep(1)
    print("")
    print("You wake up to the sun shining down on you, warming up your small tent.")
    sleep(2)
    print("")
    day += 1
    start()

#-------------------------------------------------


#start of the game script-------------------------
#clear the command line
os.system('cls')

print("--- The Golden Grove - Fishing Adventure ---")
print("e. Start New Game")
print("1. Load Game")

selection = input("Selection: ")
if selection == "e":
    print('')
    print("You sit outside the opening of a small cave. You have a tent and a lantern.")

    playerName = input("Your name is: ")

    print(f"Hello {playerName}.")
    sleep(.5)
    print('')
    start()
if selection == "1":
    print('')

    loadGame()

