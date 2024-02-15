from decouple import config


def get_api_key():
    api_key = config('API_KEY')
    # debug_mode = config('DEBUG', default=False, cast=bool)
    return str(api_key)
