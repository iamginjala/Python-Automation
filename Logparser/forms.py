from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename


class LogParserForm(FlaskForm):
    logform = FileField(validators=[FileRequired()])
    submit = SubmitField('upload')
    