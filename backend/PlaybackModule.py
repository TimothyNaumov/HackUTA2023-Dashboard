import sounddevice as sd
import soundfile as sf


data, fs = sf.read("output.mp3")
sd.play(data, fs, device=5)
sd.wait()
