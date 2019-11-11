"""
HANGMAN - CSI160 Final Project
William Alber 11/11/2019
"""
import random, sys, os, time

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

    
def play(word):
    for char in word:
        print("_", end=" ")
    
    guessed = []
    tries = 6
    while tries != 0:
        g = input("\n\nGuess a letter or input the word: ")

        # Check if guess was correct and prints remaining tries
        if g not in word:
            tries -= 1
        print("\nGuesses Remaining:", tries, end="\n\n")

        # Check for if guess is in word
        if len(g) == 1:  
            guessed.append(g)
            for char in word:
                if char in guessed:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
                    
        # Checks for word input to be correct
        elif len(g) > 1:
            if g.lower() == word:
                print("Correct! The word was", word, end=".\n")
                return
            else:
                print("Nope, that's not it. Keep guessing!")

        # Displaying incorrect guesses
        print("\n\nGuessed Letters: ", end="")
        for char in guessed:
            if char not in word:
                print(char, end=" - ")
                
            
    print("\n\nYou ran out of guesses. The word was", word + ".")
    print("Good try!\n")
    
    
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
            # Choosing random word from list
            word = random.choice(easy_words)
            play(word)
        else:
            word = random.choice(hard_words)
            play(word)

    # Change Difficulty
    if user.lower() == "d":
        print("\nChange Difficulty:\n")
        difficulty = change_difficulty(difficulty)

    # Versus Mode
    if user.lower() == "v":
        print("\nVersus Mode:\n")

        word = print("Player #1 Enter your Word: ")
        print("Good Luck Guessing, Player #2\n")
        play(word)

    # Quit
    if user.lower() == "q":
        ("\nThanks for playing!")
        sys.exit()
