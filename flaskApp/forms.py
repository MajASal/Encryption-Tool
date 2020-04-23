from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField ,IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired , Email, ValidationError, EqualTo, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()] )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    # def validate_username(self, username):
    #     user = User(username=username.data)
    #     if user:
    #         raise ValidationError('This username is taken. please choose another one')


class RegistraionForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class EncryptionForm(FlaskForm):
    encryption_input = StringField('Encryption_input', validators=[DataRequired()])
    offset = StringField('Offset', render_kw={"placeholder": "If offset is empty, a random offset will be generated for you :)"})
    encryption_type= RadioField ('Type',validators=[DataRequired()], choices=[('cesar', 'Cesar'),('mono', 'Mono')], default='cesar')

    submit = SubmitField('Encrypt')

    
