import os
import requests
import pydub
from pydub.playback import play
from io import BytesIO
from playsound import playsound
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

auth_token = os.environ["XI_API_KEY"]

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/2EiwWnXFnvU5JabPnv8n/stream"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": "660258dda9f3e33cf88a1ecdb62a1fcf",
}

data = {
    "text": "It seems like your tires are getting too thin, I would get them replaced ASAP",
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
}

response = requests.post(url, json=data, headers=headers, stream=True)

with open("output.mp3", "wb") as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
            # audio_data = BytesIO(chunk)
            # playsound(audio_data)
            # audio_file = pydub.AudioSegment.from_file(audio_data, format="mp3")
            # play(audio_file)

print("We have a response!")
playsound("output.mp3")

# # Load the audio file
# audio_file = AudioSegment.from_file("output.mp3", format="mp3")

# # Play the audio file
# play(audio_file)
