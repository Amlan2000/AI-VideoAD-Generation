from email.mime import audio
from services.rapid_client import get_audio_BPM
from services.spotify_client import SpotifyClient
from langchain.tools import tool

from services.tool_services import get_top_songs


sp=SpotifyClient()

@tool("spotify_tool")
def fetch_top_songs(query:str) -> str:
    """
    1.Fetches top trending song from Spotify.


    Returns:
    Returns songs details.

    """

    try:
        
        top_songs = get_top_songs(sp) 



        audio_features = get_audio_BPM(top_songs[0]["id"])

        return f"Songs and its features are: {top_songs[0]} : {audio_features}"
    
    except Exception as e:
        return f"Cant fetch songs. Error: {str(e)}"
    

    # Songs and its features are: {'id': '5BZsQlgw21vDOAjoqkNgKb', 'uri': 'spotify:track:5BZsQlgw21vDOAjoqkNgKb', 'name': 'DAISIES'} : {'id': '1dd6c3c77458ac41ae0dc41382fc8621', 'name': 'DAISIES', 'album': 'SWAG', 'key': 'Ab', 'mode': 'major', 'camelot': '4B', 'tempo': 110, 'duration': '2:56', 'popularity': 95, 'energy': 38, 'danceability': 80, 'happiness': 48, 'acousticness': 72, 'instrumentalness': 0, 'liveness': 11, 'speechiness': 5, 'loudness': '-9 dB'}