import random
import string

url_store = {}


def generate_short_code(length=6):
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if code not in url_store:
            return code


def shorten_url(original_url):
    code = generate_short_code()
    url_store[code] = original_url
    return code


def get_original_url(code):
    return url_store.get(code)