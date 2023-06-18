import random

# Creating the word list
word_list = ['Alert',  'Argue', 'Beach' , 'Begin' , 'Crash' , 'Crime' , 'Drink' , 'Drive' , 'Earth' , 'Empty' , 'Focus' , 'Force', 'Grass' , 'Green' , 'Heart' , 'Hotel' , 'Ideal' , 'Image', 'Juice' , 'Joint' , 'Known' , 'Knead', 'Large' , 'Light']

# Guessing a random word from the list and saving the answer
for word in word_list:
    answer = random.choice(word_list)
    print(answer)
    
# Allowing users to randomly choose a 5 letters long word in English within maximum 6 guesses
for guess in range(1,7):
    guess = input("Input a 5 letters long word in English: ").lower()
    if guess == answer.lower():
        print("Correct")
        break
    else:
        print("Wrong")


