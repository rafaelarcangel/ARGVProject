import random
name = input("What is your name? ") # The user is asked to enter the name first
print("Good Luck ! ", name)
print("Time to play 'Guess the Letters!'")
words = ['loops', 'electronics', 'engineering', 'programming',
         'statements', 'algorithm', 'hangman', 'don bosco',
         'fragments', 'python' , 'technical', 'computer',
         'pycharm', 'rafael', 'arcangel', 'pogi si raf']
word = random.choice(words) # Will choose a random word from the list
print("TAKE NOTE: SMALL LETTERS / LOWER CAPS ONLY! ")
guesses = ''
turns = 8 # Number of turns that the user can guess
while turns > 0:
    failed = 0

    for char in word:
        if char in guesses: # The characters in guesses
            print(char)

        else:
            print("_")
            failed += 1 # For every failure, 1 will be incremented in failure

    if failed == 0:


        print("You Win") # User will win the game if failure is 0 and 'You Win' will be given as output

        # this print the correct word
        print("The word is: ", word)
        break

    guess = input("guess a character:") # If user has input the wrong alphabet then it will ask user to enter another alphabet


    guesses += guess # Every input character will be stored in guesses


    if guess not in word:  # Check input with the character in word

        turns -= 1

        print("Wrong")  # If the character doesn’t match the word and  then “Wrong” will be given as output
        print("You have", + turns, 'more guesses') # This will print the number of # turns left for the user

        if turns == 0:
            print("You Loose")
            print("The word is: ", word)