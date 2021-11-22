
import random
import ascii_art
import words

def letter_match(display,j):
  flag=1
  display[j]=chosen_word[j]
  print(f"{' '.join(display)}")
  return flag

def letter_not_match(guess,chances,stages):
  print(f"You chose letter '{guess}' which is not in the word! You lose a life!!")
  chances-=1
  print(stages[chances])
  return chances

def print_result(chances,chosen_word):
  if chances==0:
    print("Game Over!!! You lose")
  else:
    print(f"You Win!!! You guessed it right the word is {chosen_word}")

def correct_guess(chosen_word,guess,j):
  if chosen_word[j] == guess and display[j]=="_":
    return True
  return False

print(ascii_art.logo)
chosen_word = random.choice(words.word_list)
print(f"Choosen word is : {chosen_word}")
stages=ascii_art.stages
chances=6
display=['_']*len(chosen_word)


while(chances!=0):
  guess = input("Guess a letter: ").lower()
  for j in range(len(chosen_word)):
    flag=-1
    if correct_guess(chosen_word,guess,j):
      flag=letter_match(display,j)
      break
  if flag==-1:
    chances=letter_not_match(guess,chances,stages)
    
  if '_' not in display:
    break
print_result(chances,chosen_word)
