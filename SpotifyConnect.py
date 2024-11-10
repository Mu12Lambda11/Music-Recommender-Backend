import spotipy
import creds
#Used to parse special characters in spotify song search
from urllib.parse import quote
from spotipy.oauth2 import SpotifyOAuth

class SpotifyConnect:
    def __init__(self):
        self.auth_manager = SpotifyOAuth(client_id=creds.spotipy_client_id,
                                         client_secret=creds.spotipy_client_secret,
                                         redirect_uri='https://localhost:8000',
                                         scope='playlist-modify-public')
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)
        self.check_and_refresh_token()

    def check_and_refresh_token(self):
        token_info = self.auth_manager.get_cached_token()
        if not token_info:
            print("No cached token found. Getting a new token.")
            token_info = self.auth_manager.get_access_token(as_dict=False)
            print(f"New Token: {token_info}")
        elif self.auth_manager.is_token_expired(token_info):
            print("Token expired. Refreshing token.")
            refreshed_token = self.auth_manager.refresh_access_token(token_info['refresh_token'])
            print(f"Refreshed Token: {refreshed_token}")
            self.sp = spotipy.Spotify(auth=refreshed_token['access_token'])
        else:
            print("Token is valid.")
    #@param List:songs_array
    #Searches for the songs in spotify's database, and adds them to a list of uris if found
    #Afterwards, generates a playlist using these found songs.
    def search_songs(self, songs_array):
        self.check_and_refresh_token()  # Ensure token is valid before making requests
        song_uris = []
        for song in songs_array:
            query = quote(f"{song['artist']} {song['title']}")
            print(f"Query: {query}")  # Print the query
            result = self.sp.search(q=query, type='track', limit=1)
            print(f"Result: {result}")
            if result['tracks']['items']:
                song_uris.append(result['tracks']['items'][0]['uri'])
            else:
                print(f"No results found for {song['title']} - {song['artist']} ({song['year']})")
        
        user_id = self.sp.current_user()['id']
        playlist = self.sp.user_playlist_create(user=user_id, name="Generated Playlist", public=True)
        self.sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
    
    def get_playlists(self):
        playlists=self.sp.current_user_playlists()
        playlists_info = [(pl['name'], pl['external_urls']['spotify']) for pl in playlists['items']]

        return playlists_info
    
    def get_playlist_tracks(self, playlist_id):
        results=self.sp.playlist_tracks(playlist_id)
        tracks = [f"{track['track']['name']} by {track['track']['artists'][0]['name']}" for track in results['items']]
        return tracks
    
    def get_user_playlist(self):
        user_playlists=self.get_playlists()

        user_input = input("Enter the name of the playlist in your library")
        matched_playlist = next((pl for pl in user_playlists if user_input.lower() in pl[0].lower()), None)

        if matched_playlist:
            playlist_url= matched_playlist[1]
            playlist_id= playlist_url.split('/')[-1]
            songs=self.get_playlist_tracks(playlist_id)
            return songs
        else:
            return "No matching playlist found"



    
    

