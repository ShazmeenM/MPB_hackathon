import itertools
import random
from colorama import Fore 
import termcolor
from termcolor import colored, cprint
colors = dict(Fore.__dict__.items()) # gets defined colors 

# Creating the word list
word_list = ['Alert',  'Argue', 'Beach' , 'Begin' , 'Crash' , 'Crime' , 'Drink' , 'Drive' , 'Earth' , 'Empty' , 'Focus' , 'Force', 'Grass' , 'Green' , 'Heart' , 'Hotel' , 'Ideal' , 'Image', 'Juice' , 'Joint' , 'Known' , 'Knead', 'Large' , 'Light']

# Guessing a random word from the list and saving the answer
for word in word_list:
    answer = random.choice(word_list)
    print(answer.lower())


# Allowing users to input a 5 letters long word in English, guess the correct word in maximum 6 attempts and telling them if the position of the letter in their entry is correct
# Color coding: Black (letter not in chosen word) Green (Letter in the word and in the correct position) Yellow (Letter in the word but not in correct position)

for guess in range(1,7):
    guess = input("Input a 5 letters long word in English: ").lower()
    position = 0
    if guess == answer.lower():
        print("Congratulations, you guessed the correct answer.")
        break
    for i, char in enumerate(guess):
        if answer[i] == guess[i]:
            print(guess.replace(guess[i], termcolor.colored(guess[i], 'green')))
            #print("Wrong answer but green letter(s) is in the word and in the correct position.")
        elif char in answer:
            print(guess.replace(guess[i], termcolor.colored(guess[i], 'yellow')))
            #print("Wrong answer but yellow letter(s) is in the word.")
        #else:
            #if char not in answer:
                #print(guess.replace(guess[i], termcolor.colored(guess[i], 'black')))
                #print("Wrong answer. None of the letters are in the word.")
    
                


