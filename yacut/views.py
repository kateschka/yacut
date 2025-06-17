import re
from http import HTTPStatus
from flask import flash, redirect, render_template
from yacut import app, db

from .models import URLMap
from .forms import URLForm
from .utils import create_url_map
from .constants import MAX_SHORT_URL_LENGTH, ErrorMessage, ErrorCategory


@app.route('/')
def index_view():
    form = URLForm()
    return render_template('main.html', form=form)


@app.route('/', methods=['POST'])
def create_id():
    form = URLForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if short_url:
            if not re.match(r'^[a-zA-Z0-9]+$', short_url):
                flash(
                    ErrorMessage.INVALID_SHORT_URL,
                    ErrorCategory.CUSTOM_ID_ERROR
                )
                return render_template('main.html', form=form)
            if len(short_url) > MAX_SHORT_URL_LENGTH:
                flash(
                    ErrorMessage.INVALID_SHORT_URL,
                    ErrorCategory.CUSTOM_ID_ERROR
                )
                return render_template('main.html', form=form)
            if URLMap.query.filter_by(short=short_url).first():
                flash(
                    ErrorMessage.SHORT_URL_ALREADY_EXISTS,
                    ErrorCategory.CUSTOM_ID_ERROR
                )
                return render_template('main.html', form=form)

        url_map = create_url_map(form.original_link.data, short_url)
        db.session.add(url_map)
        db.session.commit()
        return render_template('main.html', form=form, short_url=url_map.short)
    return render_template('main.html', form=form)


@app.route('/<string:short_url>')
def get_url(short_url):
    url_map = URLMap.query.filter_by(short=short_url).first_or_404()
    return redirect(url_map.original), HTTPStatus.FOUND
