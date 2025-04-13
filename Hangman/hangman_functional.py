#################################
# Hangman - Functional code
# Author: Dora Köhalmi
# Date: 12.04.2025
#################################
import os
import platform
import random


def clear():
    """Clears the console."""
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

# 1. Player - Input a word:
def word_input():
    """Takes a word as input or choose a random one from a list and returns it."""
    while True:
        word = input("Hi 1. Player, type a secret word or press Enter for a random one:").strip()
        if not word:
            return choose_random_word().upper()
        elif word.isalpha():
            return word.upper()
        else:
            print("Your word should only contain letters.")

def choose_random_word():
    """Chooses a random word from the built-in list."""
    mylist = ["apple", "banana", "cherry","house", "table", "chair", "pizza", "tiger", "beach", "robot", "ghost", 
              "music", "bicycle", "galaxy", "dolphin", "jungle", "cactus", "window", "fortune", "castle", "thunder", 
              "mirror", "zephyr", "awkward", "rhythm", "mystify", "oxygen", "iceberg", "knapsac", "jockey", "whizzing"]
    return random.choice(mylist)

# 2. Player - Input a letter:
def letter_input(number_of_guesses):
    """Takes a single letter as input."""
    while True:
        letter = input(f"Hi 2.Player, you have {number_of_guesses} guesses. Guess a letter:").strip().upper()    
        if letter.isalpha() and len(letter) == 1:
            return letter
        print("Please enter one single alphabetic letter.")
        

# Print the word:
def print_secret_word(secret_word, letters_to_find):
    """Prints a word with an _ for each unknown letters."""
    for i in range(len(secret_word)):
                if secret_word[i].upper() in letters_to_find:
                    print("_ ", end = "")
                else:
                    print(secret_word[i].upper() + " ", end = "")   
    print("")                 

# Print the hangman:
def print_hangman(number_of_guesses):
    """Draws a Hangman to the console, depending on the number of false guesses."""
    # Line 1
    print("_"*9)
    # Line 2
    print("|  /", end="") 
    if number_of_guesses < 8:
        print("    |")
    else:
        print()
    # Line 3        
    print("| /", end="") 
    if number_of_guesses < 8:
        print("     |")
    else:
        print()  
    # Line 4
    print("|/", end= "")
    if number_of_guesses < 7:        
        print("      O")
    else:
        print()   
    # Line 5  
    print("|", end="")  
    if number_of_guesses < 6:     
        print("       |")
    else:
        print()
    # Line 6
    print("|", end="")       
    if number_of_guesses < 5:
        print("      /", end="")
        if number_of_guesses < 4:
            print("|", end="")
            if number_of_guesses < 3:
                print("\\")
            else:
                print()    
        else:
            print()
    else:
        print()            
    # Line 7
    print("|", end="")       
    if number_of_guesses < 5:
        print("     /", end="")
        if number_of_guesses < 4:
            print(" |", end="")
            if number_of_guesses < 3:
                print(" \\")
            else:
                print()    
        else:
            print()
    else:
        print()

    # Line 8 
    print("|", end="")       
    if number_of_guesses < 2:
        print("      /", end="")
        if number_of_guesses < 1:
            print(" \\")  
        else:
            print()      
    else:
        print()


    # Line 9        
    print("|", end="")       
    if number_of_guesses < 2:
        print("     /", end="")
        if number_of_guesses < 1:
            print("   \\")  
        else:
            print()      
    else:
        print()

    # Line 10
    print("|")
    
    # Line 11
    print("|")
    
    #print("_"*9)
    #print("|  /    | ")
    #print("| /     | ")
    #print("|/      O ")
    #print("|       | ")
    #print("|      /|\ ")
    #print("|     / | \ ")
    #print("|      / \  ")
    #print("|     /   \ ")
    #print("|")
    #print("|")

def print_letters_guessed(letters_guessed):
    """Prints the letters that were already guessed."""
    print("Letters guessed: ", end="")
    if not letters_guessed:
        print()
    else:    
        for i, letter in enumerate(letters_guessed):
            if i != len(letters_guessed)-1:
                print(letter, end=", ")
            else:
                print(letter)
             
def main():
    """Hangman game."""
    secret_word = word_input()
    clear()
    #print(set(secret_word))

    # Letters in secret_word:
    letters_to_find = set(secret_word.upper()) 
    letters_guessed = []
    #print(letters_to_find)
    number_of_guesses = 8
    while number_of_guesses > 0:
        print_secret_word(secret_word, letters_to_find)
        print_hangman(number_of_guesses)
        print_letters_guessed(letters_guessed)
        #print(f"Letters guessed: {letters_guessed} ")
        letter = letter_input(number_of_guesses)
        letters_guessed.append(letter)
        #letter = input(f"Hi 2.Player, it's your turn. You have {number_of_guesses} guesses. Guess a letter:").upper()

        if letter in letters_to_find:
             letters_to_find = letters_to_find - set(letter)
             if not letters_to_find:
                 print_secret_word(secret_word, letters_to_find)
                 print("You won, 2. Player. Congratulations!")
                 break        
        elif letter in secret_word:
             print("You have already found this letter.")
        else:     
             number_of_guesses -= 1
             print(f"{letter} is not in the word")
             if not number_of_guesses:
                  print_hangman(number_of_guesses)
                  print("You lost, 2. Player.")
             
    
if __name__ == "__main__":
    main()