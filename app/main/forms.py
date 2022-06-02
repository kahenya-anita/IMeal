from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField,ValidationError,IntegerField
from wtforms.validators import Required,Email

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class AddMealForm(FlaskForm):
    name = StringField('Meal name:',validators=[Required()])
    ingredients = StringField('Ingredients',validators=[Required()])
    cost = IntegerField('Price in KSH',validators=[Required()])
    submit =SubmitField('ADD MEAL')
