import re
from http import HTTPStatus
from flask import jsonify, request
from yacut import app, db

from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .constants import MAX_SHORT_URL_LENGTH, ErrorMessage
from .views import create_url_map


@app.route('/api/id/<string:short_url>/', methods=['GET'])
def get_short_url(short_url):
    url_map = URLMap.query.filter_by(short=short_url).first()
    if url_map:
        return jsonify({'url': url_map.original}), HTTPStatus.OK
    raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)


@app.route('/api/id/', methods=['POST'])
def create_short_url():
    data = request.get_json(silent=True)
    if not data:
        raise InvalidAPIUsage(ErrorMessage.EMPTY_REQUEST)

    if 'url' not in data:
        raise InvalidAPIUsage(ErrorMessage.MISSING_URL)

    custom_id = data.get('custom_id')
    if custom_id:
        if len(custom_id) > MAX_SHORT_URL_LENGTH:
            raise InvalidAPIUsage(
                ErrorMessage.INVALID_SHORT_URL
            )
        if not re.match(r'^[a-zA-Z0-9]+$', custom_id):
            raise InvalidAPIUsage(
                ErrorMessage.INVALID_SHORT_URL
            )
        if URLMap.query.filter_by(short=custom_id).first():
            raise InvalidAPIUsage(
                ErrorMessage.SHORT_URL_ALREADY_EXISTS
            )

    url_map = create_url_map(data['url'], custom_id)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
