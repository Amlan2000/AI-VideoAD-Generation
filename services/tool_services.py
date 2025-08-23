
import json
import requests
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate



def get_top_songs(sp):
    playlist_id="0sDahzOkMWOmLXfTMf2N4N"
    url = f"{sp.base}/playlists/{playlist_id}/tracks"
    songs=[]

    res = requests.get(url,headers= sp.headers())
    res.raise_for_status()
    data=res.json()
    print("my playlist: ",data)
    items = data["items"][:3]  # taking first 3 songs
    for item in items:
        track = item["track"]
        songs.append(
            {
                "id":track["id"],
                "uri":track["uri"],
                "name":track["name"]
            }
        )
    print("songs are: ", songs)
    return songs

def get_audio_features(sp,songs_list):

    return



