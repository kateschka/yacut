from datetime import datetime
from random import choice

from flask import url_for

from yacut import db
from .constants import ALLOWED_SYMBOLS


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(2048), nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(
        db.DateTime,
        index=True,
        default=datetime.now()
    )

    def generate_short_id(self):
        return ''.join(choice(ALLOWED_SYMBOLS) for _ in range(6))

    def get_unique_short_id(self):
        short_id = self.generate_short_id()
        if URLMap.query.filter_by(short=short_id).first():
            return self.get_unique_short_id()
        return short_id

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('get_url', short_url=self.short, _external=True)
        )

    def from_dict(self, data):
        self.original = data.get('original_link')
        self.short = data.get('custom_id')
        if self.short is None:
            self.short = self.get_unique_short_id()
        return self
