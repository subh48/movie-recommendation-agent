import requests
import os
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def get_movies(genre="action"):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={genre}"
    response = requests.get(url)
    data = response.json()

    results = data.get("results", [])[:5]
    for movie in results:
        print(f"🎬 {movie['title']} ({movie.get('release_date', 'N/A')}) - Rating: {movie.get('vote_average', 'N/A')}")

# User input
genre = input("What kind of movie do you like? ")
get_movies(genre)

import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

# Ask GPT
user_input = input("You: ")
ai_response = ask_chatgpt(f"Recommend me a few {user_input} movies")
print("AI:", ai_response)

from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def get_movies_by_genre(genre):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={genre}"
    response = requests.get(url)
    data = response.json()
    return data.get("results", [])[:5]  # top 5 results

@app.route("/", methods=["GET", "POST"])
def index():
    movies = []
    if request.method == "POST":
        genre = request.form.get("genre")
        movies = get_movies_by_genre(genre)
    return render_template("index.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)