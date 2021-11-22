
import random


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

chosen_word = random.choice(word_list)

display=["_"]*len(chosen_word)

chances= 6
while(chances!=0):
  guess = input("Guess a letter: ").lower()
  for j in range(len(chosen_word)):
    flag=-1
    if chosen_word[j] == guess and display[j]=="_":
      flag=1
      display[j]=chosen_word[j]
      print(display)
      break
  if flag==-1:
      chances-=1
      print(stages[chances])
  if '_' not in display:
    break
if chances==0:
  print("Game Over!!! You lose")
else:
  print(f"You Win!!! You guessed it right the word is {chosen_word}")



