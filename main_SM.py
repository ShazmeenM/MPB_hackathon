# Importing required packages
import itertools
import random
import termcolor
from termcolor import colored, cprint

# Creating the word list
word_list = ['Alert',  'Argue', 'Beach' , 'Begin' , 'Crash' , 'Crime' , 'Drink' , 'Drive' , 'Earth' , 'Empty' , 'Focus' , 'Force', 'Grass' , 'Green' , 'Heart' , 'Hotel' , 'Ideal' , 'Image', 'Juice' , 'Joint' , 'Known' , 'Knead', 'Large' , 'Light']

# Guessing a random word from the list and saving the answer
for word in word_list:
    answer = random.choice(word_list)
    answer = answer.lower()
    print(answer)

def process_guess():
    """Function to process the guess in the Wordle game. 
    
    Input:
        input (word): 5 letters long word in English.
    
    Returns:
        Letter in black color: if the letter is not in the chosen word
        Letter in green color: letter is in the chosen word and in the correct position
        Letter in yellow color: letter is in the word but at a different position
        
    Raises:
        TypeError: if the guess includes a number or special charater.
        ValueError: if no guess was entered.
        ValueError: if the guess contains more than 5 letters.
    """              
      
    allowed_guesses = 6
    clue = ""
    while allowed_guesses>0:
        guess = input("Input a 5 letters long word in English: ").lower()
        if guess == answer.lower():
            print("Congratulations, you guessed the correct answer.")
            break
        else:
            allowed_guesses = allowed_guesses - 1
            for i, char in enumerate(guess):
                if answer[i] == guess[i]:
                    clue = colored(guess[i], 'green')
                    print(clue, "Correct letter in the right place")
                elif char in answer:
                    clue = colored(guess[i], 'yellow')
                    print(clue, "Correct letter in the wrong place")
                elif char not in answer:
                    clue = colored(guess[i], 'black')
                    print(clue, "Incorrect letter")
            if allowed_guesses == 0:
                print(" You have used maximum allowed guesses, game over!")
                
output = process_guess()

