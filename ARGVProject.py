import random
import time
import os
print()
print('''Welcome to the Slot Machine 
You'll start with P10,000. You'll be asked if you want to play.
Answer with yes/no. you can also use y/n
There is no case sensitivity, type it however you like!
To win you must get one of the following combinations:
BAR\tBAR\tBAR\t\tpays\tP12500
BELL\tBELL\tBELL/BAR\tpays\tP2000
PLUM\tPLUM\tPLUM/BAR\tpays\tP1000
ORANGE\tORANGE\tORANGE/BAR\tpays\tP500
CHERRY\tCHERRY\tCHERRY\t\tpays\tP350
CHERRY\tCHERRY\t  -\t\tpays\tP250
CHERRY\t  -\t  -\t\tpays\tP100
DATALGO\t DATALGO\tDATALGO\t\t pays\t The Jackpot! (TAKE ALL: Starting Price P50,000)
TAKE NOTE:
P500 PER ROUND!
ADDITIONAL P1,000 TO THE JACKPOT PRIZE EVERY ROUND YOU LOSE.
''')
time.sleep(5)
#Constants:
INIT_STAKE = 10000
INIT_BALANCE = 50000
ITEMS = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR", "DATALGO"]

firstWheel = None
secondWheel = None
thirdWheel = None
stake = INIT_STAKE
balance = INIT_BALANCE

def play():
    global stake, firstWheel, secondWheel, thirdWheel
    playQuestion = askPlayer()
    while(stake != 0 and playQuestion == True):
        firstWheel = spinWheel()
        secondWheel = spinWheel()
        thirdWheel = spinWheel()
        printScore()
        playQuestion = askPlayer()

def askPlayer():
    '''
    Asks the player if he wants to play again.
    expecting from the user to answer with yes, y, no or n
    No case sensitivity in the answer. yes, YeS, y, y, nO . . . all works
    '''
    global stake
    global balance
    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        if (balance <=1):
            print ("Machine balance reset.")
            balance = 50000

        print("The Jackpot is currently: P" + str(balance) + ".")
        answer = input("Would you like to play? Or check your money? (Yes or No) ")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("You ended the game with P" + str(stake) + " in your hand. Great job!")
            time.sleep(5)
            return False
        elif(answer == "check" or answer == "CHECK"):
            print ("You currently have P" + str(stake) + ".")
        else:
            print("Whoops! Didn't get that.")

def spinWheel():
   # Returns a random item from the wheel
    randomNumber = random.randint(0, 5)
    return ITEMS[randomNumber]

def printScore():
   # Prints the current score
    global stake, firstWheel, secondWheel, thirdWheel, balance
    if((firstWheel == "CHERRY") and (secondWheel != "CHERRY")):
        win = 100
        balance = balance - 100
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel != "CHERRY")):
        win = 250
        balance = balance - 250
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel == "CHERRY")):
        win = 350
        balance = balance - 350
    elif((firstWheel == "ORANGE") and (secondWheel == "ORANGE") and ((thirdWheel == "ORANGE") or (thirdWheel == "BAR"))):
        win = 500
        balance = balance - 500
    elif((firstWheel == "PLUM") and (secondWheel == "PLUM") and ((thirdWheel == "PLUM") or (thirdWheel == "BAR"))):
        win = 1000
        balance = balance - 1000
    elif((firstWheel == "BELL") and (secondWheel == "BELL") and ((thirdWheel == "BELL") or (thirdWheel == "BAR"))):
        win = 2000
        balance = balance - 2000
    elif((firstWheel == "BAR") and (secondWheel == "BAR") and (thirdWheel == "BAR")):
        win = 12500
        balance = balance - 12500
    elif((firstWheel == "DATALGO") and (secondWheel == "DATALGO") and (thirdWheel == "DATALGO")):
        win = balance
        balance = balance - win
    else:
        win = - 500
        balance = balance + 1000

    stake += win
    if win == balance:
        print ("You won the JACKPOT!!")
    if(win > 0):
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You win P' + str(win))
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You lose')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

play()