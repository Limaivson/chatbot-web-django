from decouple import config


def get_api_key():
    api_key = config('API_KEY')
    return str(api_key)
