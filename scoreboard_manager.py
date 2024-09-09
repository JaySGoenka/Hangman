import json
import os
from colorama import Fore, Style

# Load or initialize leaderboard
def load_leaderboard(file_path="leaderboard.json"):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}

# Save leaderboard
def save_leaderboard(leaderboard, file_path="leaderboard.json"):
    with open(file_path, 'w') as file:
        json.dump(leaderboard, file)

# Function to display leaderboard
def display_leaderboard(leaderboard):
    print(f"{Fore.YELLOW}Leaderboard:{Style.RESET_ALL}")
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for player, score in sorted_leaderboard:
        print(f"{Fore.CYAN}{player}: {score} points")