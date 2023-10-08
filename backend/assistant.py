import time
from livewhisper import StreamHandler
import os
import openai
import json
from openAI import generate_p1_response

with open("secrets.json", "r") as f:
    secrets = json.load(f)["openai-key"]
    openai.api_key = secrets

car_data = {
    "trips": 19,
    "miles": 144.5,
    "scores": {
        "braking": 95,
        "acceleration": 97,
        "speed": 50,
        "cornering": 70,
        "phone distraction": 80,
    },
    "lastServicedDate": {
        "brakes": "2023-01-01",
        "tires": "2023-01-01",
        "oil": "2023-01-01",
        "battery": "2023-01-01",
        "coolant": "2023-01-01",
        "air filter": "2023-01-01",
    },
    "estimatedServiceDate": {
        "brakes": {"date": "2023-07-01", "miles": 20000},
        "tires": {"date": "2029-01-01", "miles": 50000},
        "oil": {"date": "2023-07-01", "miles": 7500},
        "battery": {"date": "2026-01-01", "miles": 30000},
        "coolant": {"date": "2025-01-01", "miles": 30000},
        "air filter": {"date": "2024-01-01", "miles": 15000},
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
                "content": f"You are an automated voice assistant that helps callers understand what maintenance they need to perform on their vehicle. Respond with a short summary of the first few steps the user should take and then ask if the user would like more information. Here is the diagnostic tool of the user's car's output: {generate_p1_response(car_data)}. Do not use a bullet list or numbered list in your response.",
            },
        ]
        self.time_limit = time.time() + 60 * 2

    def analyze(self, input):  # This is the decision tree for the assistant
        # do query function here

        # take in the query and do a llm query to get the maintenance from the json
        self.messages.append({"role": "user", "content": input})
        completion = openai.ChatCompletion.create(model=model, messages=self.messages)
        output = completion.choices[0].message.content
        self.messages.append(completion.choices[0].message)
        self.speak(output)

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
