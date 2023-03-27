from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField
from wtforms.validators import DataRequired
from app.models import User

class WalletForm(FlaskForm):
    funds = DecimalField('funds', validators=[DataRequired()])
