from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, InputRequired, NumberRange


class CampaignForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    goal = FloatField(
        "Goal",
        validators=[
            InputRequired(),
            NumberRange(min=0.1, message="Enter a number greater than 0."),
        ],
    )
    picture = FileField(
        "Uptade Campaign Picture", validators=[FileAllowed(["jpeg", "png", "jpg"])]
    )
    submit = SubmitField("Post")