# Importing modules
import random as rd
 

word_list = ["aardvark", "baboon", "camel"]

chosen_word = rd.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')


# Creating blanks
display = []
for _ in range(word_length):
    display+= "_"
word_complete = False
while not word_complete:
    guess = input('Guess a letter : ').lower()
    
    # Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f'Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}')
        if letter == guess:
            display[position] = letter 
    print(display)
    if not any(letter == '_' for letter in display):
        word_complete = True
print(f'The final word is {chosen_word}!')