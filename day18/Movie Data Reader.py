# Day 18: Movie Data Reader
import json

movies_json = '''
[
    {"title": "Inception", "year": 2010, "rating": 8.8},
    {"title": "Interstellar", "year": 2014, "rating": 8.6},
    {"title": "The Dark Knight", "year": 2008, "rating": 9.0}
]
'''

# Load JSON
movies = json.loads(movies_json)

# Display Movies
for movie in movies:
    print(f"{movie['title']} ({movie['year']}) - Rating: {movie['rating']}")

# Save to file
with open("movies.json", "w") as f:
    json.dump(movies, f, indent=4)
