from services.spotify_client import SpotifyClient
from langchain.tools import tool

from services.tool_services import get_audio_features, get_top_songs


sp=SpotifyClient()

@tool("spotify_tool")
def fetch_top_songs(query:str) -> str:
    """
    1.Fetches top 3 trending songs from Spotify.


    Returns:
    Returns 3 songs details.

    """

    try:
        
        top_songs = get_top_songs(sp) 

        return f"Songs are {top_songs}"
    
    except Exception as e:
        return f"Cant fetch songs. Error: {str(e)}"