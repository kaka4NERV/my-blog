from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(5, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(5, 20)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(5, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(5, 20)])
    submit = SubmitField('Register')


class CreateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(5, 70)])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Create')


class UpdateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(5, 70)])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Update')


class DeleteForm(FlaskForm):
    submit = SubmitField('Delete')
