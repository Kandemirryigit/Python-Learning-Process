from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth



response=requests.get("https://www.billboard.com/charts/hot-100/")
soup=BeautifulSoup(response.text,"html.parser")

song_elements=soup.find_all(class_="u-max-width-230@tablet-only")



songs_list=[]
for element in song_elements[::2]:
    song_names=element.get_text(strip=True)
    songs_list.append(song_names)


sp=spotipy.Spotify(auth_manager=SpotifyOAuth(

    client_id="ec42e3696fa4489fb281200277c11a4c",
    client_secret="8da301aee62e48c9acc5a04c9a78165d",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="playlist-modify-public",

))

playlist_id="5RRdU7DI8l66oQNSnS3d2Y"


track_uris=[]

for song in songs_list:
    result=sp.search(q=song,type="track",limit=1)
    track=result["tracks"]["items"][0]
    track_uris.append(track["uri"])

sp.playlist_add_items(playlist_id,track_uris)


















    













