#1. The problem here is to create a random word from a list of words and check if it matches the users guess under a given number of tries

#2. Research: This problem can be solved with some while and conditional statements

""" 3. Planning: We want to write the code such that If word is not guessed correctly, A print Failed Attempt try again + number of tries left will be printed to screen
    After 3 tries of incorrect guesses, Then we will print the statement Out of guesses to screen """
    
#4. Now let's go with writing the code

import re
import random as rn

# Let us initialize a guess word
secret_word_list = ["Picnic", "Patrick", "list", "spongebob", "scoobydoo", "unicorn", "food", "orange", "love", "Football", "Life", "Television"]

secret_word = rn.choice(secret_word_list)



# Let us set the maximum number of attempts possible
max_attempts = 3
tries_left = 3
# Initialize attempt 
attempts = 1
out_of_guesses = False
# Take input from the user

print("Please note that for this game you have only a Maximum of 3 Attempts to get the secret word correctly. Good Luck!!!")
while (attempts <= max_attempts):
    guess_word = input("Enter a word: ")
    if guess_word.casefold() == secret_word.casefold():
        print("Hurray!!! you guessed the word correctly")
        break
    
    
    else:
        print("You have {} attempts left".format(tries_left -1))
        tries_left-= 1
        attempts += 1
        
        
else:
    out_of_guesses = True
    if out_of_guesses:
            print("Sorry! you are out of guess attempts")
    
    