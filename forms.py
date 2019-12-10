from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    ballot_name = StringField('Ballot Name', validators=[DataRequired()])
    player_list = StringField('Player List. Seperated by space', validators=[DataRequired()])
    ranker_amount = StringField('Number of Rankers')
    submit = SubmitField('Create')