import re

options = {
    'link': 'name',
    'opis': 'description',
    'css': 'css_file'
}

alphanumeric_pattern = re.compile("[A-Za-z0-9]+")


def is_alphanumeric(text: str) -> bool:
    return bool(alphanumeric_pattern.fullmatch(text))

