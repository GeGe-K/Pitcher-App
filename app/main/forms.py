from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    title = StringField('Comment title', validators = [Required()])
    review = TextAreaField('comment')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators=[Required()])
    submit = SubmitField('Submit')

class AddPitchForm(FlaskForm):
    title = StringField("Pitch Title", validators = [Required()])
    pitch = TextAreaField("Go", validators = [Required()])
    category = SelectField(
        "category",
        choices=[("pick-up", "pick-up"),("interview","interview"),("funny","funny"),("promotion","promotion"),("product","product"),("random","random")],validators = [Required()]
    )
