from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea

class ReviewForm(Form):
	review = TextAreaField('review',
		       widget=TextArea(),
		       validators=[DataRequired("Please enter your review."),
		                   Length(min=10, message="Please enter your full review.")])
	submit = SubmitField('Submit')