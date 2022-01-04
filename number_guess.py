"""
1. The Problem here is that we want to run a gueesing game such that we guess the right number from a set of random numbers
2. On Research, I found that this problem can be solved with the help of some randint and loops
3. Planning
4. Now we will start writing some codes

"""
import random as rn
# Define a random number width with the random module
random_number = rn.randint(1, 10)

# set number of attempts
max_attempts = 3


tries_left = 3
# Initialize attempt 
attempts = 1
out_of_guesses = False
# Take input from the user

print("Please note that for this game you have only a Maximum of 3 Attempts to guess the right number")
while (attempts <= max_attempts):
    
    guess_number = int(input("Enter a number: "))
    if guess_number == random_number:
        print("Hurray!!! you guessed the number correctly")
        break
    
    
    else:
        print("You have {} attempts left".format(tries_left -1))
        tries_left-= 1
        attempts += 1
        

else:
    out_of_guesses = True
    if out_of_guesses:
            print("Sorry! you are out of guess attempts")