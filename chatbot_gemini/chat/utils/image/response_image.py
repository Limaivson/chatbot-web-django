import google.generativeai as genai
from PIL import Image
from io import BytesIO
from decouple import config


class ResponseImage:
    def __init__(self):
        self.api_key = config('API_KEY')
        self.genai = genai.configure(api_key=f'{self.api_key}')
        self.model = genai.GenerativeModel('gemini-pro-vision')

    def read_image(self, uploade_image, message):
        image_data = uploade_image.read()
        image = Image.open(BytesIO(image_data))
        response = self.model.generate_content([message, image])
        response.resolve()
        return response.text
