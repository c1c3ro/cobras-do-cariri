from flask_wtf import FlaskForm
from wtforms import SubmitField

class CadastroForm(FlaskForm):
    enviar = SubmitField("Cadastrar")
