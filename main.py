# Importing modules
import random as rd
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = rd.choice(word_list)
word_length = len(chosen_word)

# setting number of lives 
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')


# Creating blanks
display = []
for _ in range(word_length):
    display+= "_"
word_complete = False
while not word_complete:
    guess = input('Guess a letter : ').lower()
    inword = False
    # Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f'Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}')
        if letter == guess:
            display[position] = letter 
            inword = True
    # Reducing number of lives if guess was not in word 
    if not inword:
        lives-=1

    # Join all the elemements in the list and turn it int a String 
    print(f"{' '.join(display)}")
    print(stages[lives])
    print(lives)
    if not any(letter == '_' for letter in display):
        word_complete = True
    if (lives == 0): 
        break
        
if word_complete:
    print(f'The final word is {chosen_word}!')
else:
    print('Game Over: you ran out of lives!')