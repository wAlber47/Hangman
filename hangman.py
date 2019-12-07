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
- Play Custom List [c]
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

# Basic Figures that coorelate to lives remaining
figures = {
    6 : "______\n|    |\n|\n|\n|\n|_______\n|       |_\n|_________|\n",
    5 : "______\n|    |\n|    0\n|\n|\n|_______\n|       |_\n|_________|\n",
    4 : "______\n|    |\n|    0\n|    |\n|\n|_______\n|       |_\n|_________|\n",
    3 : "______\n|    |\n|    0\n|   /|\n|\n|_______\n|       |_\n|_________|\n",
    2 : "______\n|    |\n|    0\n|   /|\ \n|\n|_______\n|       |_\n|_________|\n",
    1 : "______\n|    |\n|    0\n|   /|\ \n|   / \n|_______\n|       |_\n|_________|\n",
    0 : "______\n|    |\n|    0\n|   /|\ \n|   / \ \n|_______\n|       |_\n|_________|\n"
}

    
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
        print(figures[tries])
        print("\nGuesses Remaining:", tries, end="\n\n")

        # Check for if guess is in word
        if len(g) == 1:  
            guessed.append(g)
            for char in word:
                if char.isspace():
                    print(" ", end="")
                elif char in guessed:
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
            print("\nDifficulty: Hard")
            return False 
        else:
            # Stay at easy
            print("\nDifficulty: Easy")
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

        # Choosing random word from list
        if difficulty == True:
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

        word = input("Player #1 Enter your Word: ")
        for char in word:
            if char.isspace():
                word = input("Only one word allowed. Input Again: ")
                break
            else:
                continue
        print("Good Luck Guessing, Player #2\n")
        play(word.lower())

    # Custom List
    if user.lower() == "c":
        print("\nPlaying a Custom List: \n")
        print("Each word should be on a seperate line with no extra characters")
        print("Confirm that the file is located in the same directory of your file.")

        list_ = []
        file = input("\nEnter file name: ")
        try:
            with open(file, "r") as f:
                for line in f:
                    list_.append(line)
            list_ = [line.rstrip('\n') for line in open(file)]
        
            word = random.choice(list_)
            play(word)
        except FileNotFoundError:
            print("\nFile Not Found.")
            print("Check file location/spelling/extension and try again")
        
    # Quit
    if user.lower() == "q":
        ("\nThanks for playing!")
        sys.exit()
