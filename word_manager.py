import os
import random
import requests
from dotenv import load_dotenv
from hangman_words import word_list

load_dotenv()

# Fallback word list from the uploaded file
fallback_word_list = word_list

# Fetch words dynamically from an API (WordsAPI or similar)
# Fetch words dynamically from an API (WordsAPI or similar)
def fetch_movie_by_difficulty(difficulty="easy"):

    BASE_URL = 'https://api.themoviedb.org/3'
    API_KEY = os.getenv('TMDB_API_KEY')

    if not API_KEY:
        print("API key not found!")
        return fetch_fallback_movie(difficulty)

    try:
        # Fetch a list of action movies from the TMDb API
        url = f"{BASE_URL}/discover/movie"
        params = {
            'api_key': API_KEY,
            'language': 'en-US',
            'sort_by': 'popularity.desc',  # Sort movies by popularity
            'page': random.randint(1, 10),  
        }
        response = requests.get(url, params=params)
        response_data = response.json()

        # Check if the response contains any results
        if response.status_code != 200 or 'results' not in response_data:
            print(f"API Error: {response_data.get('status_message', 'Unknown error')}")
            return fetch_fallback_movie(difficulty)

        movies = response_data.get('results', [])
        # print(f"API response: {movies}")  # Debug API response

        if not movies:
            print("No movies found in API response.")
            return fetch_fallback_movie(difficulty)  # Fallback if no movies are found

        # Filter movie titles based on difficulty
        if difficulty == "easy":
            word_list_api = [movie['title'] for movie in movies if 4 <= len(movie['title']) <= 7]
        elif difficulty == "medium":
            word_list_api = [movie['title'] for movie in movies if 7 <= len(movie['title']) <= 12]
        elif difficulty == "hard":
            word_list_api = [movie['title'] for movie in movies if 11 <= len(movie['title']) <= 17]
        else:
            word_list_api = [movie['title'] for movie in movies]  # Default fallback to all titles

        # print(f"Filtered movie list for {difficulty} difficulty: {word_list_api}")  # Debug filtered movie list

        # Return a random title based on the difficulty
        return random.choice(word_list_api).lower() if word_list_api else fetch_fallback_movie(difficulty)

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return fetch_fallback_movie(difficulty)  # Fallback in case of error


# Fallback to the hangman_words word list if API fails
def fetch_fallback_movie(difficulty):
    if difficulty == "easy":
        fallback_list = [movie for movie in word_list if 4 <= len(movie) <= 7]
    elif difficulty == "medium":
        fallback_list = [movie for movie in word_list if 7 <= len(movie) <= 12]
    elif difficulty == "hard":
        fallback_list = [movie for movie in word_list if 11 <= len(movie) <= 17]
    else:
        fallback_list = word_list  # Default fallback
    
    # Return a random fallback movie
    return random.choice(fallback_list).lower() if fallback_list else "minions"


if __name__ == "__main__":
    print(fetch_movie_by_difficulty("easy"))
    print(fetch_movie_by_difficulty("medium"))
    print(fetch_movie_by_difficulty("hard"))
    print(fetch_movie_by_difficulty("invalid"))
