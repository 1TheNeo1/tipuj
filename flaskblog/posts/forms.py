from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Utakmica:', validators=[DataRequired()])
    #content = StringField('Tvoj Tip: ', validators=[DataRequired(), Length(min=1, max=5)])
    content = SelectField('Tvoj Tip: ', choices=[('1', '1'), ('x', 'x'), ('2', '2'), ('3+', '3+'), ('0-3', '0-3'), ('GG3+', 'GG3+'), ('GG', 'GG') ])
    submit = SubmitField('Tipuj')