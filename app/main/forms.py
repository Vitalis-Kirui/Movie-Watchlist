from flask_wtf import FlaskForm
#helps us create form classes
from wtforms import StringField, TextAreaField, SubmitField
#help us creating fields
from wtforms.validators import Required
#helps us with validation before user submits the review

class ReviewForm(FlaskForm):
    """
    Review class that inherits from FlaskForm
    """
    
    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')