from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo


class SigninForm(FlaskForm):
    email1 = StringField('Email', validators=[DataRequired()])
    paskey = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit1 = SubmitField('Sign In')

    
class RegisterForm(FlaskForm):
    accesslevel = SelectField('Access level', choices=[],validators=[DataRequired()])
    gender = SelectField('Gender', choices=[],validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register Order')

class OrderForm(FlaskForm):
    size = SelectField('Size', choices=[])
    ordernum = SelectField('Number of items', choices=[])
    email = StringField('Email', validators=[DataRequired()])
    creit = IntegerField('Creit Card',validators=[DataRequired()])
    name = IntegerField('Name',validators=[DataRequired()])
    expiredata = StringField('Expiry date', validators=[DataRequired()])
    submit = SubmitField('Submit Order')







