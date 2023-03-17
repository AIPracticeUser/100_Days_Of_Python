## Hangman Game
- Aim: Complete Challenges and Familiarize with Random Module

### Rules of Game

Hangman is a guessing game for two or more players. One player thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting letters within a certain number of guesses. Originally a Paper-and-pencil game, there are now electronic versions.

### How to break down a complex problem into a flowchart
<img width="588" alt="Solution+-+Hangman+Flowchart+1" src="https://user-images.githubusercontent.com/100339175/226004348-a298b92b-c8ef-4664-bedb-39086d4608de.png">

### Challenge 1 - Picking a Random Words and checking answers
Update the word list to use the 'word_list' from hangman_words.py

```
import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for word in chosen_word:
  if word == guess:
    print("Right")
  else:
    print("Wrong")
```
RESULT: 

![image](https://user-images.githubusercontent.com/100339175/226020939-5ff13fbf-04fa-4b33-a298-e55e12c2b9fc.png)


### Challenge 2 - Replacing Blanks with Guesses
```
#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_len = len(chosen_word)
for letter in range(word_len):
  display.append("__")
print(display)
guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for position in range(word_len):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
```
RESULT:

![image](https://user-images.githubusercontent.com/100339175/226029769-d8f6bb45-35be-411e-a4eb-74283e1efd70.png)
