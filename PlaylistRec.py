def playlist_rec(playlist_tracks):
    tracklist_string='\n'.join(playlist_tracks)
    prompt = """Use the following tracklist to produce a spotify-based playlist of similar songs or recommended songs.
            Do not include a title for the playlist, include only the songs.
            Format the songs as following without deviation:  Title /// Album ### Artist (Year)""", tracklist_string
    return prompt