import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="ec42e3696fa4489fb281200277c11a4c",
    client_secret="8da301aee62e48c9acc5a04c9a78165d",
    redirect_uri="http://localhost:3000/callback",
    scope="user-library-read"
))




with open("C:/Users/CASPER/Desktop/python_projects/project62/song_names2.csv","a",encoding="UTF-8") as f:
    offset=0
    for x in range(2):
        results=sp.current_user_saved_tracks(limit=50,offset=offset)
        for item in results['items']:
            track = item['track']
            song = track['name']
            artist = track['artists'][0]['name']
            f.writelines(f"{song}-{artist}\n")
        offset+=50

    