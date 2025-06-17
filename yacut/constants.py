import string


ALLOWED_SYMBOLS = string.ascii_letters + string.digits

MAX_SHORT_URL_LENGTH = 16
MAX_URL_LENGTH = 2048

DEFAULT_SHORT_URL_LENGTH = 6


class ErrorMessage:
    EMPTY_REQUEST = 'Отсутствует тело запроса'
    MISSING_URL = '"url" является обязательным полем!'
    INVALID_SHORT_URL = 'Указано недопустимое имя для короткой ссылки'
    SHORT_URL_ALREADY_EXISTS = (
        'Предложенный вариант короткой ссылки уже существует.'
    )
