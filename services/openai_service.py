from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def ask_model(user_message: str) -> str:
    response = client.responses.create(
        model="gpt-5.4",
        input=user_message
    )
    return response.output_text