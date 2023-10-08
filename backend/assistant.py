from livewhisper import StreamHandler
import os


# significant credit to Nik Stromberg - nikorasu85@gmail.com - MIT 2022 - copilot
class Assistant:
    def __init__(self):
        self.running = True
        self.talking = False

    def analyze(self, input):  # This is the decision tree for the assistant
        # do query function here
        pass

    def speak(self, text):
        self.talking = True  # if I wanna add stop ability, I think function needs to be it's own object
        # print(f"\n\033[92m{text}\033[0m\n")
        # add eleven labs functionality here
        # and call this from the analyze function
        self.talking = False


def main():
    try:
        AIstant = Assistant()  # voice object before this?
        handler = StreamHandler(AIstant)
        handler.listen()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        print("\n\033[93mQuitting..\033[0m")
        if os.path.exists("dictate.wav"):
            os.remove("dictate.wav")


if __name__ == "__main__":
    main()  # by Nik
