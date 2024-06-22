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

end_of_game = False
word_list = ["ardvark", "baboon", "carmel"]

choosen_word = random.choice(word_list)
print (f"The solution is : {choosen_word}")

display = []
word_length = len(choosen_word)
for _ in range(word_length):
    display += '_'
print(display)

lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(stages[lives])