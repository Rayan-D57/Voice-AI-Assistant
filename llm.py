import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.ClientV2(
    api_key=os.getenv("COHERE_API_KEY")
)

SYSTEM_PROMPT = """
You are a helpful AI assistant.

Rules:

- Always answer in the SAME language used by the user.
- If the user speaks Arabic, answer in Arabic.
- If the user speaks English, answer in English.
- Keep answers natural and conversational.
"""

def ask_ai(message):

    response = co.chat(
        model="command-a-03-2025",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.message.content[0].text