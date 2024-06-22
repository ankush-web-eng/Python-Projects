import requests
from bs4 import BeautifulSoup

year = input("Enter Year in format as YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{year}"
page = requests.get(URL)
playlist_kit = page.text
soup = BeautifulSoup(playlist_kit,"html.parser")
song_boxes= soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_boxes]
# print(song_name)
# for i in song_names:
#     print(i)
p = 1
with open(file="songs.txt", mode="w", encoding="utf-8") as songs_playlist:
    for i in song_names:
        songs_playlist.write(f"{p}) {i}\n")
        p+=1