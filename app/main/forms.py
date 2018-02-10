from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    category = SelectField('Pitch Category',choices=[('music','music'),
                                                        ('life','life'),
                                                        ('pickup','Pickup Pitch'),
                                                        ('interview','Interview Pitch'),
                                                        ('production','Production Pitch'),
                                                        ('promotion','Promotion Pitch')], validators=[Required()])
    author = StringField('Author', validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you',validators = [Required()])
    submit = SubmitField('Submit')

class FeedbackForm(FlaskForm):
    author = StringField('Author', validators=[Required()])
    comment = TextAreaField('Feedback', validators=[Required()])
    submit= SubmitField('Submit')
