from email.mime import audio
import json
import os

from flask import request
import librosa
import requests
from sqlalchemy import exists
from services.rapid_client import get_audio_BPM
from services.spotify_client import SpotifyClient
from langchain.tools import tool

from services.tool_services import get_top_songs


sp=SpotifyClient()

@tool("audio_generation_tool")
def audio_generation() -> str:
    """
    Complete audio workflow:
    1. Fetch trending song from Spotify
    2. Analyze with librosa for precise BPM and beat positions
    4. Return song info + beat data + audio file path
    """

    try:
        
        top_songs = get_top_songs(sp) 
        top_song= top_songs[0]

        # if not top_song["preview_url"]:
        #      return json.dumps({"error": "No preview available", "song": top_song["name"]})
        
        # os.makedirs("assets/songs",exists_ok=True)

        # song_name= top_song["name"].replace(" ","_").replace("/","_")
        # audio_file = f"assets/songs/{song_name}_preview.mp3"
        # print(f"Downloading: {top_song['name']} by {top_song['artist']}")
        # response = requests.get(top_song["preview_url"])

        # with open(audio_file,'wb') as f:
        #     f.write(response.content)

        audio_file= f"assets/music/song1.mp3"
        # Analyze with librosa
        print(f"Analyzing beats...")
        y, sr = librosa.load(audio_file)
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beats, sr=sr)
        
        result = {
            # "song_name": top_song["name"],
            # "artist": top_song["artist"],
            "bpm": round(float(tempo), 1),
            "beat_positions": beat_times.tolist()[:15],
            "audio_file": audio_file,
            "duration": len(y) / sr, 
            "success": True
        }
        
        print(f"✅ Analysis complete: {result['bpm']} BPM, {len(result['beat_positions'])} beats detected")
        return json.dumps(result)
        
    except Exception as e:
        print(f"❌ Error in audio analysis: {str(e)}")
        return json.dumps({"error": str(e), "success": False})

        # audio_features = get_audio_BPM(top_songs[0]["id"])

    #     return f"Songs and its features are: {top_songs[0]} : {audio_features}"
    
    # except Exception as e:
    #     return f"Cant fetch songs. Error: {str(e)}"
    

    # Songs and its features are: {'id': '5BZsQlgw21vDOAjoqkNgKb', 'uri': 'spotify:track:5BZsQlgw21vDOAjoqkNgKb', 'name': 'DAISIES'} : {'id': '1dd6c3c77458ac41ae0dc41382fc8621', 'name': 'DAISIES', 'album': 'SWAG', 'key': 'Ab', 'mode': 'major', 'camelot': '4B', 'tempo': 110, 'duration': '2:56', 'popularity': 95, 'energy': 38, 'danceability': 80, 'happiness': 48, 'acousticness': 72, 'instrumentalness': 0, 'liveness': 11, 'speechiness': 5, 'loudness': '-9 dB'}