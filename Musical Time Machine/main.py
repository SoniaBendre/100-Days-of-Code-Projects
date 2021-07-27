from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "874f6c16538a4cc28d455d1229a7bb30"
CLIENT_SECRET = "6144801b20564ac7ae5648b27e31fb28"
REDIRECT_URI = 'http://example.com'
SCOPE = "playlist-modify-private"

date = input("Input a date in the format YYYY-MM-DD ")
url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
songs = [song.getText() for song in soup.find_all(name="span", class_="chart-element__information__song")]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        show_dialog=True))

USER_ID = sp.current_user()["id"]

results = sp.user_playlist_create(user=USER_ID, name=f"{date} Top 100", public=False)

PLAYLIST_ID = results["id"]

song_uris = []

for song in songs:
    try:
        second_results = sp.search(q=f"track: {song} year: {date[:4]}", type="track")
        song_uri = second_results["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"{song} doesn't exist in spotify. Skipped")
    else:
        song_uris.append(song_uri)

sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=song_uris)

