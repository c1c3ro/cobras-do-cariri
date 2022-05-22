from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    usuario = StringField('Usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    