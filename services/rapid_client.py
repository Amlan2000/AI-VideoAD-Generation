import requests

from dotenv import load_dotenv

load_dotenv()

RAPID_API_KEY = os.getenv("RAPID_API_KEY")

def get_audio_BPM(uri:str):

    url = f"https://track-analysis.p.rapidapi.com/pktx/spotify/{uri}"

    headers = {
	"x-rapidapi-key": RAPID_API_KEY,
	"x-rapidapi-host": "track-analysis.p.rapidapi.com"
}

    response = requests.get(url, headers=headers)

    return response.json()

