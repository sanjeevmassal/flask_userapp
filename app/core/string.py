from unidecode import unidecode
from slugify import slugify as str_slug


def slugify(string, seperator='-', max_length=220):
    slug = str_slug(unidecode(string), seperator)
    if len(slug) > max_length:
        slug = slug[:max_length]
    return slug
