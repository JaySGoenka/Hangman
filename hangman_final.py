import random
import os
import sys



from hangman_words import word_list

from hangman_art import logo, stages

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    # Initial game setup
    end_of_game = False
    lives = 6

   
    display = ["_" for _ in range(word_length)]

    print(logo)

    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        
        if guess in display:
            print(f"You've already guessed {guess}")
        
        guess_was_correct = False
        
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                guess_was_correct = True
        
        if not guess_was_correct and guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The correct word was: {chosen_word}")
        
        print(f"{' '.join(display)}")
        
        if "_" not in display:
            end_of_game = True
            print("You win.")
        
        if not end_of_game:
            print(stages[lives])

def main():
    while True:
        clear_screen()
        play_game()
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break 

if __name__ == "__main__":
    main()
