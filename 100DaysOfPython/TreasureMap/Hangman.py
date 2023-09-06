import random
animal_list = ["ardvark", "baboon", "snake", "mouse", "parrot", "tiger", 
"elephant", "giraffe", "dolphin", "koala", "panda", "zebra", "lion", 
"cheetah", "kangaroo", "rhinoceros", "otter", "penguin", "octopus", "hippopotamus"]
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

chosen_word = random.choice(animal_list)

display = []
lifeDict = {
    6:stages[0],
    5:stages[1],
    4:stages[2],
    3:stages[3],
    2:stages[4],
    1:stages[5],
}
for _ in chosen_word:
    display.append('_')
lives = 6
letters_guessed = []
endOfGame = False
while not endOfGame:
    guess = input('Guess a letter: ').lower()
    letters_guessed += guess
    index = 0
    letter_found = False
    for letter in chosen_word:
        if letter == guess:
            display[index] = letter
            letter_found = True
        index += 1
    if not letter_found:
        lives -= 1
        print(lifeDict.get(lives))
        print(f"Chances left: {lives}")
    print("*" * 20)
    print(lifeDict.get(lives))
    print(f"{' '.join(display)}")
    print(f"Current guessed letters: {' '.join(letters_guessed)}")
    print("*" * 20)
    
    
    if "_" not in display:
        endOfGame = True
        print(f"Word was {chosen_word}! You got it!")
    elif lives == 0:
        endOfGame = True
        print(stages[6])
        print(f"Word was {chosen_word}, Try again!")
