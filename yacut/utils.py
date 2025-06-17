from random import choice
from .constants import ALLOWED_SYMBOLS, DEFAULT_SHORT_URL_LENGTH


def generate_short_id():
    return ''.join(
        choice(ALLOWED_SYMBOLS) for _ in range(DEFAULT_SHORT_URL_LENGTH)
    )


def get_unique_short_id():
    # Импорт модели для избежания циклического импорта
    from .models import URLMap

    short_id = generate_short_id()
    if URLMap.query.filter_by(short=short_id).first():
        return get_unique_short_id()
    return short_id


def create_url_map(original_url, custom_id=None):
    # Импорт модели для избежания циклического импорта
    from .models import URLMap
    
    url_map = URLMap()
    url_map.original = original_url
    url_map.short = custom_id if custom_id else get_unique_short_id()
    return url_map