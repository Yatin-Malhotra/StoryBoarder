import requests
import json
import base64
from PIL import Image
from io import BytesIO

def storyboard_generator(text, model, i):
    API_KEY = "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"

    # The type of images the user wanted to be generated, such as realistic or anime
    if (model == 'realistic'):
        model = 'image-alpha-001'
    else:
        model = 'image-anime-001'

    # Send a request to the Dall-E 2 API with the given text
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        },
        data=json.dumps({
            "model": model,
            "prompt": f"Storyboard image for the text: {text}",
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
        image.save(f"storyboardimage{i + 1}.jpg")
    except KeyError:
        print("Error: data not found in API response.")
        image_url = None

# storyboard_generator("Pat is a fat guy", "realistic", 1)
