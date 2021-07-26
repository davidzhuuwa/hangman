# Importing modules
import random as rd
 

word_list = ["aardvark", "baboon", "camel"]

chosen_word = rd.choice(word_list)


# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display
# For each letter in the chosen word, add a "_" to 'display'

display = []
for i in range(0,len(chosen_word)):
    display.append('_')
print(display)

guess = input('Guess a letter : ').lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
i = 0
for letter in chosen_word:
    if guess == letter:
        display[i] = letter
    else:
        print('Wrong')
    i+=1
print(display)