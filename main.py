# Programmer: Chris Heise (crheise@icloud.com)
# School: New Mexico Highlands University
# Course: BSSD 3410 Applied Algorithms & Architecture
# Instructor: Jonathan Lee
# Date: 9 March 2023
#
# Program: Midterm Project
# Purpose: Use Text Analysis and Dynamic Programming to create a fill-in-the-blank game.
# File: main.py

# All three novels were downloaded from Project Gutenberg
# 'The Great Gatsby' by F. Scott Fitzgerald
# URL: https://www.gutenberg.org/ebooks/64317
# 'Dracula' by Bram Stoker
# URL: https://www.gutenberg.org/ebooks/345
# 'The Adventures of Sherlock Holmes' by Arthur Conan Doyle
# URL: https://www.gutenberg.org/ebooks/1661
# CHANGELOG:
# - Deleted any content before the first chapter
# - Deleted any content after the end of the story

from text_functions import *
from edit_distance import editDistDP


def main():
    options = ["dracula.txt", "gatsby.txt", "sherlock.txt"]

    print("\nThis is a game where you pick a famous novel you think you know well;")
    print("then you try to guess a missing word from a random sentence in that novel.")
    print("Press Q to quit.\n")

    # This is the main play loop
    playing = True
    while playing:
        print("Select a novel:")
        print("1. 'Dracula' by Bram Stoker")
        print("2. 'The Great Gatsby' by F. Scott Fitzgerald")
        print("3. 'The Adventures of Sherlock Holmes' by Arthur Conan Doyle")
        novel = input("Your choice ==> ")

        guessing = False
        match novel:
            case "1":
                guessing = True
            case "2":
                guessing = True
            case "3":
                guessing = True
            case "Q":
                playing = False
            case "q":
                playing = False
            case _:
                print("I'm sorry, I don't understand that selection. Try Again.")

        # If the user made a valid selection, get the sentences from the text
        sentences = ""
        if guessing:
            index = int(novel)
            sentences = process_text(options[index-1], "utf-8")

        # This is the inner play loop (for an individual book)
        while guessing:
            # Pick a random word from a random sentence
            random_sentence = get_random_sentence(sentences)
            missing_word = get_random_word(random_sentence)

            print(f"\nYour Sentence:\n{random_sentence.replace(missing_word, '<blank>')}")
            guess = input("Fill in the blank ==> ")

            # Compare the two words
            guess = guess.lower()
            missing_word = missing_word.lower()
            results = editDistDP(guess, missing_word, len(guess), len(missing_word))

            # Report how they did (results is number of characters to edit for guess to be correct)
            if results == 0:
                print(f"Good job! You guessed: '{guess}', and it was: '{missing_word}'!")
            elif results < len(missing_word)/2:
                print(f"You were close! You guessed: '{guess}' and the missing word was: '{missing_word}'!")
            else:
                print(f"You guessed: '{guess}', but the missing word was: '{missing_word}'!")

            print("Keep guessing? (Y to continue, N to change Novels, Q to quit)")
            keep_playing = input("==> ")

            match keep_playing.lower():
                case "y":
                    continue
                case "n":
                    guessing = False
                case "q":
                    playing = False
                    guessing = False
                case _:
                    print("I didn't understand that, let's keep playing.")


if __name__ == '__main__':
    main()
