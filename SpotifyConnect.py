import spotipy
import creds
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=creds.spotipy_client_id,
                                               client_secret=creds.spotipy_client_secret,
                                               redirect_uri='https://localhost:3000',
                                               scope='playlist-modify-public'))

#@param List:songs_array
#Searches for the songs in spotify's database, and adds them to a list of uris if found
#Afterwards, generates a playlist using these found songs.
def search_songs(songs_array):
    song_uris=[]
    for song in songs_array:
        query = f"track:{song['track']} artist:{song['artist']} year:{song['year']}"
        result= sp.search(q=query, type='track', limit=1)
        if result ['tracks']['items']:
            song_uris.append(result ['tracks']['items']['uri'])
    
    user_id= sp.current_user()['id']
    playlist = sp.user_playlist_create(user=user_id, name="Generated Playlist", public=True)    
    sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)    
    
    

