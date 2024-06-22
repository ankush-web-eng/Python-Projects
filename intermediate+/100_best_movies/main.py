import requests
from bs4 import  BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_kit = response.text

soup = BeautifulSoup(web_kit, 'html.parser')
all_movies = soup.find_all(name="h3", class_="title")
movies_titles = []
for movie in all_movies:
    movies_titles.append(movie.text)
# print(movies_titles)
movies_titles.reverse()
with open(file="movies.txt", mode="w", encoding="utf-8") as file_:
    for title in movies_titles:
        file_.write(f"{title}\n")