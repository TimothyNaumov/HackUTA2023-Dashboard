import time
from livewhisper import StreamHandler
import os
import openai
import json
from openAI import generate_p1_response
from AudibleResponse import speak
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

car_data = {
    "trips": 19,
    "miles": 144.5,
    "scores": {
        "braking": 68,
        "acceleration": 44,
        "speed": 60,
        "cornering": 33,
        "phone distraction": 80,
    },
    "lastServicedDate": {
        "brakes": "2023-01-01",
        "tires": "2021-01-01",
        "oil": "2023-05-01",
        "battery": "2023-01-01",
        "coolant": "2023-01-01",
        "air filter": "2023-01-01",
    },
    "timeUntilService": {
        "brakes": {"days": "250", "miles": 14780},
        "tires": {"date": "53", "miles": 1260},
        "oil": {"date": "210", "miles": 4892},
        "battery": {"date": "745", "miles": 27688},
        "coolant": {"date": "384", "miles": 18990},
        "air filter": {"date": "126", "miles": 2344},
    },
    "vehicle": {
        "vehicleType": "Sedan",
        "vehicleMake": "Toyota",
        "vehicleModel": "Camry",
        "vehicleYear": 2012,
        "miles": 60000,
    },
}


model = "gpt-3.5-turbo"


# significant credit to Nik Stromberg - nikorasu85@gmail.com - MIT 2022 - copilot
class Assistant:
    def __init__(self):
        self.running = True
        self.talking = False
        self.messages = [
            {
                "role": "system",
                "content": f"You are an excited customer service rep at an auto maintenance company. When a user talks to you, give them the most pertinent advice relevant to their car. They may give information, or you may have to read the diagnostic tool. Here is the diagnostic tool's output: {generate_p1_response(json.dumps(car_data))}. Do not use a bullet list or numbered list in your response. Do not respond with more than 2 sentences.",
            },
        ]
        self.time_limit = time.time() + 60 * 2

    def analyze(self, input):  # This is the decision tree for the assistant
        # do query function here
        if input == "":
            return
        # take in the query and do a llm query to get the maintenance from the json
        self.messages.append({"role": "user", "content": input})
        completion = openai.ChatCompletion.create(model=model, messages=self.messages)
        output = completion.choices[0].message.content
        self.messages.append(completion.choices[0].message)
        self.speak(output)

        pass

    def speak(self, text):
        self.talking = True  # if I wanna add stop ability, I think function needs to be it's own object
        speak(text)
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
