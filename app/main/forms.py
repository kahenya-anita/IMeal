from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField,ValidationError
from wtforms.validators import Required,Email

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')