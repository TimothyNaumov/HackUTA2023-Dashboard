import openai
import json
from typing import List

with open("secrets.json", "r") as f:
        secrets = json.load(f)["openai-key"]
        openai.api_key = secrets

def generate_p1_response(jsons: str) -> List[object]:
    

    model = "gpt-3.5-turbo"

    messages = [
        {
            "role": "system",
            "content": "You are a diagnostic tool that determines a recommended action given this data from a vehicle. Respond with short phrase summarizing what you would recommend servicing",
        },
        {
            "role": "user", 
            "content": jsons
        },
    ]


    completion = openai.ChatCompletion.create(
        model=model, messages=messages
    )

    return completion

def generate_p2_response(str1: str, str2: str) -> List[object]:

    prompt = f"""You are an automated voice assistant that helps callers understand what maintenance they need to perform on their vehicle.
    
    The diagnostic tool said "{str1}".

    Respond with a short summary of the first few steps the user should take and then ask if the user would like more information. Do not use a bullet list or numbered list in your response"""

    model = "gpt-3.5-turbo"

    messages = [
        {
            "role": "system",
            "content": prompt,
        },
        { 
            "role": "user", 
            "content": str2
        },
    ]


    completion = openai.ChatCompletion.create(
        model=model, messages=messages
    )

    return completion


if __name__ == "__main__":
    y = "How much would a repair cost?"

    x = {
            "trips": 19,
            "miles": 144.5,
            "scores": {
                "braking": 95,
                "acceleration": 97,
                "speed": 50,
                "cornering": 70,
                "phone distraction": 80
            },
            "lastServicedDate": {
                "brakes": "2023-01-01",
                "tires": "2023-01-01",
                "oil": "2023-01-01",
                "battery": "2023-01-01",
                "coolant": "2023-01-01",
                "air filter": "2023-01-01"
            },
            "estimatedServiceDate": {
                "brakes": {
                "date": "2023-07-01",
                "miles": 20000
                },
                "tires": {
                "date": "2029-01-01",
                "miles": 50000
                },
                "oil": {
                "date": "2023-07-01",
                "miles": 7500
                },
                "battery": {
                "date": "2026-01-01",
                "miles": 30000
                },
                "coolant": {
                "date": "2025-01-01",
                "miles": 30000
                },
                "air filter": {
                "date": "2024-01-01",
                "miles": 15000
                }
            },
            "vehicle": {
                "vehicleType": "Sedan",
                "vehicleMake": "Toyota",
                "vehicleModel": "Camry",
                "vehicleYear": 2012,
                "miles": 60000
            }
        }
    
        
    
    test_output = generate_p1_response(
        json.dumps(x)
    )

    test_output2 = generate_p2_response(
        test_output.choices[0].message.content, y
    )   

    print('p1: ' + test_output.choices[0].message.content + '\n')
    print('p2: ' + test_output2.choices[0].message.content + '\n')
    # print(test_output.choices[0].message.content)

    # write the output to a json file
    # with open("output.json", "w") as f:
    #     f.write(json.dumps(test_output))