"""
HANGMAN - CSI160 Final Project
William Alber 11/11/2019
"""
import random, sys

print("Hello! Welcome to Hangman!")
print("Please refer to the menu and select an option.")
menu_text = """
Please Select an option: 
- Start Solo Game [s]
- Change Difficulty [d]
- Two Player Versus Mode [v]
- Quit [q]
"""

# Difficulty (True is easy, False is hard)
difficulty = True

# List for easy difficulty
easy_words = ["hello", "dragon", "pizza", "women", "brake", "snake",
              "mouse", "spoon", "ocean", "house", "apple", "swing",
              "circle", "flower", "jacket", "pillow", "spider"]

# List for hard difficulty
hard_words = ["awkward", "axion", "buzzwords", "buckaroo", "croquet",
              "duplex", "dwarves", "espionage", "equip", "fjord",
              "haphazard", "hyphen", "injury", "kayak", "juicy",
              "length", "microwave", "nightclub", "pixel", "queue",
              "stronghold", "transcript", "transgress", "voodoo",
              "waltz", "witchcraft", "yummy", "zigzag", "zodiac"]

def play(words):
    # Choosing random word from list
    word = words[random.randint(0, len(words))]
    for char in word:
        print("_", end=" ")

    print(word)
    
    guessed = []
    for i in range(0, 6):  # Hangman has six guesses
        g = input("\nGuess a letter: ")
        if len(g) == 1:  # Testing that input is char
            guessed.append(g)
            for char in word:
                print()  # Formatting
                if char in guessed:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
            print("\n\nGuessed Letters:", guessed)
            print()  # Formatting
    
def change_difficulty(difficulty):
    if difficulty == True:
        print("You are currently on easy mode.")
        change = input("Switch to hard mode: [y/n] ")
        if change.lower() == "y":
            # Change to hard
            ("\nDifficulty: Hard")
            return False 
        else:
            # Stay at easy
            ("\nDifficulty: Easy")
            return True
    if difficulty == False:
        print("You are currently on hard mode.")
        change = input("Switch to easy mode: [y/n] ")
        if change.lower() == "y":
            # Change to easy
            print("\nDifficulty: Easy")
            return True
        else:
            print("\nDifficulty: Hard")
            # Stay at hard
            return False
        
            
while True:
    print(menu_text)
    user = input()

    # Start Game
    if user.lower() == "s":
        print("\nSolo Game:\n")
        if difficulty == True:
            play(easy_words)
        else:
            play(hard_words)

    # Change Difficulty
    if user.lower() == "d":
        print("\nChange Difficulty:\n")
        difficulty = change_difficulty(difficulty)

    # Versus Mode
    if user.lower() == "v":
        print("\nVersus Mode:\n")

    # Quit
    if user.lower() == "q":
        ("\nThanks for playing!")
        sys.exit()
