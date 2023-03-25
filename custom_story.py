import openai
openai.api_key = "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"

from PIL import Image
import requests
from io import BytesIO

def Custom_Script(script: str, genre: str) -> str:
    
    text_prompt = "Write me a movie script for the genre " + genre + " with the description of: " + script

    chatgpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text_prompt}],
            temperature=0.1,
            max_tokens=2000,
            top_p=0.95)

    response = chatgpt_response['choices'][0]['message']['content'].strip()

    return response
