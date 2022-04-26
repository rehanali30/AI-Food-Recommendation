from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[Email(), DataRequired()])
    login = SubmitField("Login")

class SignupForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[Email(), DataRequired()])
    submit = SubmitField("Submit")