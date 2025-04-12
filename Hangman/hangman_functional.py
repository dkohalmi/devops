#################################
# Hangman - Functional code
# Author: Dora Köhalmi
# Date: 12.04.2025
#################################
import os
import platform


def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

# 1. Player - Input a word
def word_input():
    word = input("Hi 1. Player, it's your turn. Type in a secret word:")
    return word

# Print the word:
def print_secret_word(secret_word, letters_to_find):
    for i in len(secret_word):
                if secret_word[i] in letters_to_find:
                    print("_ ", end = "")
                else:
                    print(secret_word[i].uppercase() + " ", end = "")    


# 2. Player - Guess a letter

def main():
    secret_word = word_input()
    clear()
    print(set(secret_word))

    print("_ "*len(secret_word))
    # Letters in secret_word:
    letters_to_find = set(secret_word) 

    number_of_guesses = 8
    while number_of_guesses > 0:
        letter = input(f"Hi 2.Player, it's your turn. You have {number_of_guesses} guesses. Guess a letter:")

        if letter in letters_to_find:
             letters_to_find = letters_to_find - set(letter)
             if not letters_to_find:
                 print("You won, 2. Player. Congratulations!")
                 break        
        elif letter in secret_word:
             print("You have already found this letter.")
        else:     
             number_of_guesses -= 1
             print(f"{letter} is not in the word")
             if not number_of_guesses:
                  print("You lost, 2. Player.")
             
    
if __name__ == "__main__":
    main()