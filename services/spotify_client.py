import requests
from services.auth import get_access_token


class SpotifyClient:
    
    def __init__(self):
        self.base="https://api.spotify.com/v1"
        self.access_token=get_access_token()
        print("token is: ",self.access_token)

    def headers(self):
        return {
            "Authorization":f"Bearer {self.access_token}",
            "Content-Type":"application/json",
        }


    def top_songs(self):
        playlist_id="0sDahzOkMWOmLXfTMf2N4N"
        url = f"{self.base}/playlists/{playlist_id}/tracks"
        # url = f"{self.base}/me/playlists"
        songs=[]

        res = requests.get(url,headers= self.headers())
        res.raise_for_status()
        data=res.json()
        print("my playlist: ",data)
        items = data["items"][:3]  # take first 3 songs
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
