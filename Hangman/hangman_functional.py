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

def main():
    secret_word = word_input()
    clear()
    print(secret_word) 

if __name__ == "__main__":
    main()