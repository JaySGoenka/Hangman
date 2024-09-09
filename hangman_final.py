import random
import os
import time
from colorama import Fore, Style, init
from hangman_art import logo, stages
from word_manager import fetch_movie_by_difficulty
from scoreboard_manager import load_leaderboard, save_leaderboard, display_leaderboard

# Initialize colorama
init(autoreset=True)

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to reveal a letter as a hint
def reveal_letter(word, display, used_letters):
    remaining_letters = [letter for letter in word if letter not in used_letters and letter not in display]
    if remaining_letters:
        hint_letter = random.choice(remaining_letters)
        for i, letter in enumerate(word):
            if letter == hint_letter:
                display[i] = letter
        used_letters.add(hint_letter)
        return True
    return False

# Function to calculate score based on difficulty and time taken
def calculate_score(difficulty, lives_left, time_taken):
    base_score = 10 if difficulty == "easy" else 20 if difficulty == "medium" else 30
    time_penalty = (time_taken // 10)
    score = base_score + max(0, 6 - lives_left) * 2 - time_penalty
    return max(0, score)

# Main game function
def play_game():
    leaderboard = load_leaderboard()
    player_name = None  # Variable to store the player's name

    while True:
        if not player_name:  # Only ask for the name if not already set
            player_name = input("Enter your name: ").strip()

        difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()

        while True:  # Loop to keep the player playing until they lose
            chosen_word = fetch_movie_by_difficulty(difficulty)
            word_length = len(chosen_word)

            # Initial game setup
            end_of_game = False
            lives = 6
            display = ["_" for _ in range(word_length)]  # Initialize the display with dashes
            used_letters = set()
            hints_left = 3
            start_time = time.time()

            print(logo)
            print(f"{Fore.GREEN}Welcome {player_name}! Let's play Hangman!")
            print(f"{' '.join(display)}")  # Display the word with dashes

            while not end_of_game:
                guess = input("Guess a letter or type 'hint' to use a hint: ").lower()

                if guess == 'hint' and hints_left > 0:
                    if reveal_letter(chosen_word, display, used_letters):
                        hints_left -= 1
                        print(f"{Fore.GREEN}Hint used! Letters remaining: {hints_left}")
                    else:
                        print(f"{Fore.RED}No more letters to reveal.")
                elif guess in used_letters:
                    print(f"{Fore.YELLOW}You've already guessed {guess}")
                else:
                    used_letters.add(guess)
                    guess_was_correct = False
                    for position in range(word_length):
                        letter = chosen_word[position]
                        if letter == guess:
                            display[position] = letter
                            guess_was_correct = True

                    if not guess_was_correct:
                        lives -= 1
                        print(f"{Fore.RED}You guessed {guess}, that's not in the word. You lose a life.")

                print(f"{' '.join(display)}")  # Display the updated word
                print(stages[lives])

                if "_" not in display:
                    # Player guessed the word correctly, continue with a new word
                    time_taken = round(time.time() - start_time, 2)
                    score = calculate_score(difficulty, lives, time_taken)
                    print(f"{Fore.GREEN}Congratulations {player_name}, you guessed the word!")
                    print(f"{Fore.GREEN}Time taken: {time_taken} seconds. Score: {score}")
                    leaderboard[player_name] = leaderboard.get(player_name, 0) + score

                    # Save the leaderboard and load a new word automatically
                    save_leaderboard(leaderboard)
                    display_leaderboard(leaderboard)

                    # Break out of the inner loop to get a new word without asking the player
                    break

                elif lives == 0:
                    # Player lost
                    print(f"{Fore.RED}You lost! The word was {chosen_word}. Better luck next time!")
                    end_of_game = True
                    break

            # Check if the player lost, and ask if they want to restart or a new player can start
            if lives == 0:
                save_leaderboard(leaderboard)
                display_leaderboard(leaderboard)

                # Ask if the player wants to restart or if a new player should start
                new_game = input("Do you want to let a new player start or quit the game? (new/quit): ").strip().lower()
                if new_game == 'new':
                    player_name = None  # Reset player_name to allow a new player to enter their name
                    break  # Exit the loop for a new player to start
                else:
                    print("Thank you for playing! The game will now end.")
                    exit() # Exit the game

# Start the game
if __name__ == "__main__":
    play_game()
