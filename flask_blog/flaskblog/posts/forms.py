from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired(message='This field is required')])
    content = TextAreaField('Content', [validators.DataRequired(message='This field is required')])
    submit = SubmitField('Post')
    


