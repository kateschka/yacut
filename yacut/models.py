from datetime import datetime
from flask import url_for

from yacut import db
from .constants import (
    MAX_SHORT_URL_LENGTH,
    MAX_URL_LENGTH,
)
from .utils import get_unique_short_id


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_URL_LENGTH), nullable=False)
    short = db.Column(
        db.String(MAX_SHORT_URL_LENGTH), nullable=False, unique=True
    )
    timestamp = db.Column(
        db.DateTime,
        index=True,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            'url': self.original,
            'short_link': url_for(
                'get_url', short_url=self.short, _external=True
            )
        }

    def from_dict(self, data):
        self.original = data.get('original_link')
        self.short = data.get('custom_id')
        if self.short is None:
            self.short = get_unique_short_id()
        return self
