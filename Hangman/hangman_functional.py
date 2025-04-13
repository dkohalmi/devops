#################################
# Hangman - Functional code
# Author: Dora Köhalmi
# Date: 12.04.2025
#################################
import os
import platform
import random


def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

# 1. Player - Input a word
def word_input():
    word = input("Hi 1. Player, it's your turn. Type in a secret word or hit Enter for a random one:")
    if not word:
        word = choose_random_word()
    return word

def choose_random_word():
    mylist = ["apple", "banana", "cherry","house", "table", "chair", "pizza", "tiger", "beach", "robot", "ghost", 
              "music", "bicycle", "galaxy", "dolphin", "jungle", "cactus", "window", "fortune", "castle", "thunder", 
              "mirror", "zephyr", "awkward", "rhythm", "mystify", "oxygen", "iceberg", "knapsac", "jockey", "whizzing"]
    return random.choice(mylist)

# Print the word:
def print_secret_word(secret_word, letters_to_find):
    for i in range(len(secret_word)):
                if secret_word[i] in letters_to_find:
                    print("_ ", end = "")
                else:
                    print(secret_word[i].upper() + " ", end = "")   
    print("")                 

# Print the hangman:
def print_hangman(number_of_guesses):
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

# 2. Player - Guess a letter

def main():
    secret_word = word_input()
    clear()
    #print(set(secret_word))

    # Letters in secret_word:
    letters_to_find = set(secret_word) 

    number_of_guesses = 8
    while number_of_guesses > 0:
        print_secret_word(secret_word, letters_to_find)
        print_hangman(number_of_guesses)
        letter = input(f"Hi 2.Player, it's your turn. You have {number_of_guesses} guesses. Guess a letter:")

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