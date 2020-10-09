from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange, InputRequired
from food.models import User
from flask_login import current_user


class OrderForm(FlaskForm):
    amount = FloatField(
        "Amount",
        validators=[
            InputRequired(),
            NumberRange(min=0.01, message="Please enter an amount greater than 0.")
        ])
    submit = SubmitField("Donate")