from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
class ImageGenerator:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def generate_image(self, prompt):
        response = self.client.images.generate(
          model="dall-e-3",
          prompt=prompt,
          size="1024x1024",
          quality="standard",
          n=1,
        )

        image_url = response.data[0].url
        return image_url