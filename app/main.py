import os
from openai import OpenAI
import requests

GAS_ENDPOINT = "https://script.google.com/macros/s/AKfycbxNzqeepKifrMa79MXHwMmvFows9alWKBDP1aY56ioY4v2Q3TJifcps6WfR_1nAW67ieA/exec"

def create_reservation(data: dict):
    response = requests.post(GAS_ENDPOINT, json=data)
    return response.json()

if __name__ == "__main__":
    reservation = {
        "name": "テスト太郎",
        "date": "2026-02-15",
        "time": "19:00",
        "people": 2,
        "note": "カウンター希望"
    }

    result = create_reservation(reservation)
    print(result)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(question: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=question
    )
    return response.output_text

if __name__ == "__main__":
    user_input = input("質問を入力してください: ")
    answer = ask_ai(user_input)
    print("AIの回答:", answer)
