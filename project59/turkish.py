from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

response=requests.get("https://www.shazam.com/tr-tr/charts/top-50/t%C3%BCrkiye/istanbul")
soup=BeautifulSoup(response.text,"html.parser")

song_elements=soup.find_all(class_="common_link__7If7r")

songs_list=[]

i=1
for x in range(50):
    song=song_elements[i].text
    songs_list.append(song)
    i+=3


sp=spotipy.Spotify(auth_manager=SpotifyOAuth(

    client_id="ec42e3696fa4489fb281200277c11a4c",
    client_secret="8da301aee62e48c9acc5a04c9a78165d",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="playlist-modify-public",

))

user_id=sp.current_user()["id"]
playlist=sp.user_playlist_create(user_id,"creative",public=True,description="dream")

track_uris=[]

for song in songs_list:
    result=sp.search(q=song,type="track",limit=1)
    track=result["tracks"]["items"][0]
    track_uris.append(track["uri"])

sp.playlist_add_items(playlist["id"],track_uris)
