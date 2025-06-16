import re
from flask import flash, redirect, render_template
from yacut import app, db

from .models import URLMap
from .forms import URLForm
from .utils import create_url_map


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
                    'Указано недопустимое имя для короткой ссылки',
                    'custom_id_error'
                )
                return render_template('main.html', form=form)
            if len(short_url) > 16:
                flash(
                    'Указано недопустимое имя для короткой ссылки',
                    'custom_id_error'
                )
                return render_template('main.html', form=form)
            if URLMap.query.filter_by(short=short_url).first():
                flash(
                    'Предложенный вариант короткой ссылки уже существует.',
                    'custom_id_error'
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
    return redirect(url_map.original), 302
