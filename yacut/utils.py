from yacut.models import URLMap


def create_url_map(original_url, custom_id=None):
    url_map = URLMap()
    url_map.original = original_url
    url_map.short = custom_id if custom_id else url_map.get_unique_short_id()
    return url_map