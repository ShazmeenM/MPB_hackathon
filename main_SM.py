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

# The nested loop below will allow users to input a 5 letters long word in English, guess the correct word in maximum 6 attempts and tell them if they have 1) guessed the correct word, 2) guessed the correct letter in the right place, 3) guess the correct letter in the wrong place.
# Color coding is used to give clues i.e., Black (letter not in the chosen word), Green (Letter is in the word and in the correct position) and Yellow (Letter is in the word but at a different position)

for guess in range(1,7):
    guess = input("Input a 5 letters long word in English: ").lower()
    clue = ""
    if guess == answer.lower():
        print("Congratulations, you guessed the correct answer.")
        break
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
                

# Trying to combine nested loops in a function

def main():
    for guess in range(1,7):
        guess = input("Input a 5 letters long word in English: ").lower()
        clue = ""
        if guess == answer.lower():
            print("Congratulations, you guessed the correct answer.")
            break
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
                

