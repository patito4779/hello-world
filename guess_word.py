#1. The problem here is to Take an input word and check if it matches secret word under a given number of tries

#2. Research: This problem can be solved with some while and conditional statements

""" 3. Planning: We want to write the code such that If word is not guessed correctly, A print Failed Attempt try again + number of tries left will be outputted to screen
    After 3 tries of incorrect guesses, Then we will print the statement Out of guesses to screen """
    
#4. Now let's go with writing the code

import re

# Let us initialize a guess word
secret_word = "Picnic"
secret_word = secret_word.lower()

# Let us set the maximum number of attempts possible
max_attempts = 3
tries_left = 3
# Initialize attempt 
attempts = 1
out_of_guesses = False
# Take input from the user


while (attempts <= max_attempts):
    guess_word = input("Enter a word: ")
    if guess_word.casefold() == secret_word.casefold():
        print("Hurray you got the correct word succesfully")
    
    
    else:
        print("You have {} attempts left".format(tries_left -1))
        tries_left-= 1
        attempts += 1
        
        
        
    
        
        
else:
    out_of_guesses = True
    if out_of_guesses:
            print("Sorry you are out of guess attempts")
    
    
