import soundfile as sf
import sounddevice as sd
import asyncio


def greet():
    data, fs = sf.read("Greeting.mp3")
    sd.play(data, fs)
    sd.wait()
