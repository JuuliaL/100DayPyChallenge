# Replit clear function

from replit import clear
import random
import sys  
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = ["_"] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose.")
            print(f'The chosen word was {chosen_word}.')
            sys.exit()  

    print(' '.join(display))

    if "_" not in display:
        print("You win.")
        sys.exit()  

    print(stages[lives])
