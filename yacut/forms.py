from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, Regexp


class URLForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 2048, message='Слишком длинная ссылка')])
    custom_id = StringField(
        'Короткая ссылка',
        validators=[
            Optional(),
            Length(1, 16, message='Слишком длинный идентификатор'),
            Regexp(r'^[a-zA-Z0-9]+$', message='Некорректный идентификатор')
        ])
    submit = SubmitField('Создать')