from services.spotify_client import SpotifyClient
from langchain.tools import tool


sp=SpotifyClient()

@tool("spotify_tool")
def fetch_top_songs(query:str) -> str:
    """
    Fetches top 3 trending songs from Spotify.


    Returns:
    Returns 3 songs details.

    """

    try:
        
        top_songs = sp.top_songs()

        return f"Songs are {top_songs}"
    
    except Exception as e:
        return f"Cant fetch songs. Error: {str(e)}"