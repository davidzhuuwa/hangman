# Importing modules
import random as rd
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

chosen_word = rd.choice(word_list)
word_length = len(chosen_word)

print(logo)
# setting number of lives 
lives = 6

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Creating blanks
display = []
guess_list = []
for _ in range(word_length):
    display+= "_"
word_complete = False
while not word_complete:
    guess = input('Guess a letter : ').lower()
    inword = False

    # using clear() to clear output between guesses
    clear() 
    
    # Checking that user hasn't already guessed the letter
    if guess not in guess_list:
        guess_list.append(guess)
    else:
        print(f'The letter {guess} has already been guessed.')
        continue 

    # Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f'Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}')
        if letter == guess:
            display[position] = letter 
            inword = True

    # Reducing number of lives if guess was not in word 
    if not inword:
        print(f'The letter {guess} was not in the word')
        lives-=1

    # Join all the elements in the list and turn it int a String 
    print(f"{' '.join(display)}")
    print(stages[lives])
    if not any(letter == '_' for letter in display):
        word_complete = True
    if (lives == 0): 
        break
if word_complete:
    print(f'The final word is {chosen_word}! You win!')
else:
    print('Game Over: you ran out of lives!')