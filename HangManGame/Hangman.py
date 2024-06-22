import os
import random

from hangman_word import word_list
choosen_word = random.choice(word_list)
print (f"The solution is : {choosen_word}")

end_of_game = False
lives = 6

from hangman_art import logo,stages
print(logo)

display = []
word_length = len(choosen_word)
for _ in range(word_length):
    display += '_'
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('clear')

    if guess in display:
        print(f"You already guess {guess}")

    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in choosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(stages[lives])