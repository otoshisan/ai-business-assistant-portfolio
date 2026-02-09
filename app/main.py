import os
from openai import OpenAI

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
