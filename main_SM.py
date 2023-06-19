import random

# Creating the word list
word_list = ['Alert',  'Argue', 'Beach' , 'Begin' , 'Crash' , 'Crime' , 'Drink' , 'Drive' , 'Earth' , 'Empty' , 'Focus' , 'Force', 'Grass' , 'Green' , 'Heart' , 'Hotel' , 'Ideal' , 'Image', 'Juice' , 'Joint' , 'Known' , 'Knead', 'Large' , 'Light']

# Guessing a random word from the list and saving the answer
for word in word_list:
    answer = random.choice(word_list)
    print(answer)
    
# Allowing users to input a 5 letters long word in English, guess the correct word in maximum 6 attempts and telling them if the position of the letter in their entry is correct
for guess in range(1,7):
    guess = input("Input a 5 letters long word in English: ").lower()
    if guess == answer.lower():
        print("Correct")
        break
    else:
        guess_str = str(guess)
        for i, val in enumerate(str(answer)):
            if guess_str[i] == val:
                print("The position num {} is correct". format(i+1))
        print("Your guess is incorrect")


