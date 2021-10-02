import re
import requests

from config import api_token, base_url

options = {
    'link': 'name',
    'opis': 'description',
    'css': 'css_file'
}
headers = {"Authorization": f"Bearer {api_token}"}
alphanumeric_pattern = re.compile("[A-Za-z0-9]+")


def is_alphanumeric(text: str) -> bool:
    return bool(alphanumeric_pattern.fullmatch(text))


def send_update_request(payload):
    r = requests.post(base_url, data=payload, headers=headers)
    return r

