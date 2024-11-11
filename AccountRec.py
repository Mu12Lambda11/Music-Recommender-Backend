def account_rec(top_artists):
    artists_string='\n'.join(top_artists)
    
    prompt="""Use the following top artists for a given Spotify user to produce a spotify-based playlist of similar songs or recommended songs.
            Do not include a title for the playlist, include only the songs.
            Do not include any
            Format the songs as following without deviation:  Title /// Album ### Artist (Year)
            
            Top Artists: %s """ %(artists_string)
            
    return prompt