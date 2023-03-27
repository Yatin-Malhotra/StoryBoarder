import requests
import json
import base64
from PIL import Image
from io import BytesIO

def image_generator(text, model, i):
    API_KEY = 'ENTER KEY HERE, MINE IS SECRET'

    # The type of images the user wanted to be generated, such as realistic or anime
    if (model == 'realistic'):
        prompt_text = f"A hyperdetailed realistic image without any text for the text: {text}"
    else:
        prompt_text = f"Cartoon like image without any text for the text: {text}"

    # Send a request to the Dall-E 2 API with the given text
    # "prompt": f"Storyboard image for the text: {text}",
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        },
        data=json.dumps({
            "model": 'image-alpha-001',
            "prompt": prompt_text,
            "num_images": 1,
            "size": "512x512",
            "response_format": "url"
        })
    )

    # Retrieve the URL of the generated image from the API response
    try:
        # print(response.json())
        image_url = response.json()["data"][0]["url"]
        # Download the image from the URL 
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        image.save(f"image{i + 1}.jpg")
    except KeyError:
        print("Error: data not found in API response.")
        image_url = None

# storyboard_generator("Pat is a fat guy", "realistic", 1)
