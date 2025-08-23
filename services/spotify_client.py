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

