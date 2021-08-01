from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User




class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.InputRequired(),validators.Length(min=2,max=20)])
    email = StringField('Email', [validators.InputRequired(), validators.Email()])  
    password = PasswordField('Password', [validators.InputRequired()])
    confirm_password = PasswordField('Confirm Password', [validators.InputRequired(), validators.EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is already taken. Please choose a different one')

            
    def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email is already taken. Please choose a different one')


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.InputRequired(), validators.Email()])
    password = PasswordField('Password', [validators.InputRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', [validators.InputRequired(),validators.Length(min=2,max=20)])
    email = StringField('Email', [validators.InputRequired(), validators.Email()])    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'], 'File doesnot have an approved extension: jpg, png!')])
    submit = SubmitField('Update')

    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first() 
            if user:
                raise ValidationError('This Username is already taken. Please choose a different one')

        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This Email Id is already taken. Please choose a different one')

class ResetForm(FlaskForm):
    email = StringField('Email', [validators.InputRequired(), validators.Email()])
    submit = SubmitField('Request Password Reset')


    def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()
            if user is None:
                raise ValidationError('This Email Id doesn\'t exsit. You must register first')


class ResetPasswordForm(FlaskForm):
     password = PasswordField('Password', [validators.InputRequired()])
     confirm_password = PasswordField('Confirm Password', [validators.InputRequired(), validators.EqualTo('password')])
     submit = SubmitField('Reset Password')
