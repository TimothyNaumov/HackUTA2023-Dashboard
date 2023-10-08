import os
import requests
from pydub.playback import play
from playsound import playsound
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

xi_api_key = os.environ["XI_API_KEY"]

voice_ID = "ThT5KcBeYPX3keUQqHPh"

CHUNK_SIZE = 1024
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_ID}/stream"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": xi_api_key,
}

data = {
    "text": "Your tires are estimated to last until 2029 or 50,000 miles. Currently, your vehicle has 60,000 miles. Your tires should still be in good condition. Regular inspections are recommended to ensure safety.",
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
}

response = requests.post(url, json=data, headers=headers, stream=True)

with open("output.mp3", "wb") as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)

print("We have a response!")
playsound("output.mp3")
