import os
import requests
from dotenv import load_dotenv
import sounddevice as sd
import soundfile as sf
import time

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

sound_device = 11


def speak(message):
    data = {
        "text": message,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.25, "similarity_boost": 0.5},
    }

    response = requests.post(url, json=data, headers=headers, stream=True)

    with open("output.mp3", "wb") as f:
        start_time = time.time()  # record the start time
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    elapsed_time = time.time() - start_time  # calculate the elapsed time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")  # print the elapsed time

    data, fs = sf.read("output.mp3")
    sd.play(data, fs, device=sound_device)
    sd.wait()
