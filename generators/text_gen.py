from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
class PostGenerator:
    def __init__(self, api_key, tone, topic):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.tone = tone
        self.topic = topic

    def generate_post(self):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            #response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Ты высококвалифицированный SMM специалист, который будет помогать "
                        "в генерации текста для постов с заданной тебе тематикой и заданным тоном. "
                        #"Ответ должен быть в формате json."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Сгенерируй пост для соцсетей с темой {self.topic}, используя тон: {self.tone}"
                    )
                }
            ]
        )
        return response.choices[0].message.content
    def generate_post_image_description(self):
        response = self.client.chat.completions.create(
          model="gpt-4o",
          messages=[
            {"role": "system", "content": "Ты ассистент, который составит промпт для нейросети, которая будет генерировать изображения. Ты должен составлять промпт на заданную тематику."},
            {"role": "user", "content": f"Сгенерируй изображение для соцсетей с темой {self.topic}"}
          ]
        )
        return response.choices[0].message.content