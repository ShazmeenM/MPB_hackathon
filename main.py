# Importing required packages
import itertools
import random
import termcolor
from termcolor import colored, cprint
import string

# Creating the word list
word_list = ['Alert',  'Argue', 'Beach' , 'Begin' , 'Crash' , 'Crime' , 'Drink' , 'Drive' , 'Earth' , 'Empty' , 'Focus' , 'Force', 'Grass' , 'Green' , 'Heart' , 'Hotel' , 'Ideal' , 'Image', 'Juice' , 'Joint' , 'Known' , 'Knead', 'Large' , 'Light']


def get_random_word(word_list):
    """
    Function to guess a random word from a list of strings.
    
    Args:
        word_list (list): A list of 5-letter words.
    
    Returns:
        A random word from the word_list.
        
    """
    for word in word_list:
        return random.choice(word_list)

# Calling the get_random_word function and storing the random word as answer
answer = get_random_word(word_list)
answer = answer.lower()

def process_guess():
    """
    Function to process the guess in the Wordle game. The function allows 6 attempts to guess the answer.
    The function will break when the user guess the correct answer or the maximum guesses have been reached.  
    
    Input:
        input (guess): 5 letters long word in English.
    
    Returns:
        Letter in black color: if the letter is not in the correct answer
        Letter in green color: letter is in the correct answer and in the correct position
        Letter in yellow color: letter is in the correct answer but at a different position
        
    Raises:
        ValueError: if the number of letters in the guess is not equal to 5.
        TypeError: if any character in the guess is not a string.
    """              
      
    allowed_attempts = 6
    
    # creating a placeholder for storing each character in the guess in the desired colors
    clue = ""
    
    while allowed_attempts>0:
        guess = input("Input a 5 letters long word in English: ").lower()
        if len(guess) != 5:
            raise ValueError("The guess must be 5 letters long")
        if not guess.isalpha():
            raise TypeError("The guess must only contain letters")  
        if guess == answer.lower():
            print("Congratulations, you guessed the correct answer")
            break
        else:
            allowed_attempts = allowed_attempts - 1
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
            if allowed_attempts == 0:
                print(" You have used maximum allowed guesses, game over!")

# Call the function to process the guess                
process_guess()

