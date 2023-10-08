import os
import requests
from dotenv import load_dotenv
import sounddevice as sd
import soundfile as sf
import time
from time import sleep
import random
import asyncio

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

sound_device = 5

# Get a list of all the mp3 files in the fillerphrases directory
fillerphrases_dir = "./filler_phrases"
mp3_files = [f for f in os.listdir(fillerphrases_dir) if f.endswith(".mp3")]


async def play_filler():
    print("playing filler")
    while True:
        fillerphrase_file = os.path.join(fillerphrases_dir, random.choice(mp3_files))
        fillerphrase_data, fillerphrase_fs = sf.read(fillerphrase_file)
        sd.play(fillerphrase_data, fillerphrase_fs)
        await asyncio.sleep(
            len(fillerphrase_data) / fillerphrase_fs
        )  # Sleep until filler phrase is finished playing


async def get_transcription(message):
    data = {
        "text": message,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.25, "similarity_boost": 0.5},
    }

    response = requests.post(url, json=data, headers=headers, stream=True)

    with open("AIResponse.mp3", "wb") as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    data, fs = sf.read("AIResponse.mp3")
    sd.play(data, fs)
    sd.wait()


async def speak(message):
    # Start the filler audio loop
    filler_task = asyncio.create_task(play_filler())

    # Wait for a short while to ensure filler audio starts
    await asyncio.sleep(0.1)

    # Get the TTS transcription
    await get_transcription(message)

    # Once the transcription is ready, stop the filler audio
    filler_task.cancel()
    try:
        await filler_task
    except asyncio.CancelledError:
        pass
