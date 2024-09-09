# Hangman Game Project

This project is a terminal-based Hangman game that dynamically fetches movie titles as the words for players to guess. The game allows players to compete against each other and keep track of scores using a persistent leaderboard. Players can choose between different difficulty levels, with corresponding word lengths and scoring systems. The game continues until a player runs out of lives, at which point a new player can start or the game can be quit.

## Features

- Dynamic Word Fetching: The game uses an external API to fetch movie titles for players to guess ensuring a wide variety of words for each difficulty level.
- Multiple Difficulty Levels: Players can choose between easy, medium, or hard difficulty, with the length of movie titles adjusted accordingly.
- Leaderboard: A persistent leaderboard keeps track of player scores across sessions, allowing players to see their performance compared to others.
- Hints System: Players can use a limited number of hints to reveal letters in the word.
- Multiple Players: After a game ends, a new player can start a game, or the game can be quit entirely.
- Scoring Based on Difficulty: The scoring system takes into account the difficulty level chosen by the player, the time taken to guess the word, and the number of lives remaining.
- ASCII Art: The game displays stages of a hangman figure, progressing as the player loses lives.
- Clean Interface with Color: Using the colorama library, the game provides color-coded messages, making it more engaging.

## Game Flow

- Start a New Game:
When the game starts, the player is prompted to enter their name.
They are then asked to choose a difficulty level: easy, medium, or hard.
- Guess the Word:
The player attempts to guess letters in the movie title. For each incorrect guess, the player loses a life, and the hangman figure progresses.
Players can also type hint to reveal a random letter, but hints are limited.
- Win or Lose:
If the player guesses all the letters in the movie title, they win, and the score is calculated based on difficulty, time taken, and lives remaining.
If the player runs out of lives, they lose, and the word is revealed.
- End of Game:
After a game ends, a new player can start a game or the current session can be ended.

## Scoring System

The scoring system is based on:

Difficulty Level:

Easy: Base score of 10

Medium: Base score of 20

Hard: Base score of 30

Time Taken: A penalty is applied based on the time taken to guess the word.

Lives Remaining: Players earn bonus points for each life they have remaining.

## Dependencies

requests: To fetch movie titles from the TMDB API.

colorama: For colored output in the terminal.

python-dotenv: For managing environment variables like API keys.
