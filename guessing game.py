### Number Guessing Game ###

# Import Packages
import random    # To create random number
import sys       # To allow program exit
import time      # To allow pauses in program

# Intitialize Variables
answer = random.randint(1, 25)
guess = 0
count = 0
playagain = 'y'

# Greeting
print("Hello Player!")
time.sleep(2)
print("Welcome to the Number Guessing Game")

# Loop Until the player does not want to play anymore
while playagain != 'n':

    # Game Rules
    time.sleep(2)
    print("We have chosen a number between 1 and 25")
    time.sleep(2)
    print("Please guess the number.")
    print("If you guess wrong, we will give you a hint if the number is higher or lower.")
    print("Keep guessing until you choose the correct number.")
    print("We will let you know how many guesses it took to choose the number.")
    time.sleep(6)

    # Player interaction
    print("Enter your number now!")

    # Assign players guess to the variable "guess"
    guess = eval(input())
    count += 1

    # Check to see if the value entered is an inetger
    #while type(guess) != int
    #if type(guess) = float
    #    then print("Please enter an integer between 1 and 25")
    #guess = input()
    #elif type(guess) = string
    #    then print("We are guessing numbers not words. Enter an integer between 1 and 25")
    #guess = input()
    #end

    #Logic
    while answer != guess:
        if guess < answer:
            print("You did not guess correctly. Choose again! Hint: the answer is greater than what you guessed")
        elif guess > answer:
            print("You did not guess correctly. Choose again! Hint: the answer is less than what you guessed")
        guess = eval(input())
        count += 1

    if guess == answer:
        print("Hooray!!! You guessed the correct number, %d" % guess)
    time.sleep(2)
    print("It took you %d number of guesses to get the correct number" % count)
    time.sleep(2)
    print("Would you like to play again? Enter 'y' for yes, or 'n' for no")

    playagain = input()
    answer = random.randint(1, 25)
    guess = 0
    count = 0  

if playagain == 'n':
    print("Thanks for playing!!! Come play again soon!")
    
# End the program
sys.exit()


