import google.generativeai as genai
from decouple import config


class ResponseText:
    def __init__(self):
        self.api_key = config('API_KEY')
        self.genai = genai.configure(api_key=f'{self.api_key}')
        self.model = genai.GenerativeModel('gemini-pro')

    def responseGeminai(self, text):
        response = self.model.generate_content(str(text))
        return response.text
