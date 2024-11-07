import requests
from bs4 import BeautifulSoup
import random

#URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
URL = "https://www.empireonline.com/movies/features/best-movies-2/"
FILE = "movies_to_watch.txt"

# Get the website
website = requests.get(url=URL)
soup = BeautifulSoup(markup=website.text, features="html.parser")

# Get the movie tags
movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

# Get the movie titles and reverse the list
movie_titles = [movie.get_text() for movie in movies]
movie_titles.reverse()

# Write movie list to file
with open(FILE, "w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")

# Choose a random movie
print(random.choice(movie_titles))
