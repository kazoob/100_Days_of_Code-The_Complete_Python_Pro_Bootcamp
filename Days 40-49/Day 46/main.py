import requests
from bs4 import BeautifulSoup
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pprint

BB_URL_BASE: str = "https://www.billboard.com/charts/hot-100"
SP_MAX_TRACKS = 5

date: str = ""

# Get date from user, verify format.
while not re.match('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', date):
    date = input("Which year do you want to travel to? YYYY-MM-DD: ")

year: int = int(date.split("-")[0])

#
# Billboard
#

# Website information.
bb_url = f"{BB_URL_BASE}/{date}"
bb_header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}

# Get website using requested date.
bb_response = requests.get(url=bb_url, headers=bb_header)
bb_soup = BeautifulSoup(markup=bb_response.text, features="html.parser")

# Get the track span elements.
tracks = bb_soup.select("li ul li h3")

# Get the track titles.
track_titles: list = [track.get_text().strip() for track in tracks]
pprint.pp(track_titles)
print()

#
# Spotify
#

# Authentication.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["SPOTIFY_CLIENT_ID"],
                                               client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
                                               redirect_uri="https://example.com",
                                               scope="user-library-read playlist-modify-private"))

# Get user id.
sp_user_id: str = sp.current_user()["id"]
print(f"Spotify user id: {sp_user_id}")
print()

# Track URI list.
sp_track_uris: list = []

# Determine number of tracks to search.
sp_num_tracks: int
if SP_MAX_TRACKS >= len(track_titles):
    sp_num_tracks = len(track_titles)
else:
    sp_num_tracks = SP_MAX_TRACKS

# Search for tracks.
for track in track_titles[:sp_num_tracks]:
    sp_result = sp.search(q=f"track: {track} year: {year}", type="track", limit=1)
    try:
        track_uri = sp_result["tracks"]["items"][0]["uri"]
        sp_track_uris.append(track_uri)
    except IndexError:
        print(f"Track {track} ({year}) not found, skipping.")

pprint.pp(sp_track_uris)
print()

# Create playlist
sp_playlist = sp.user_playlist_create(user=sp_user_id, name=f"{date} Billboard 100", public=False)
pprint.pp(sp_playlist)
print()
sp_playlist_id = sp_playlist["id"]
print(f"Playlist ID: {sp_playlist_id}")
print()

# Add tracks to playlist
sp.playlist_add_items(playlist_id=sp_playlist_id, items=sp_track_uris)
