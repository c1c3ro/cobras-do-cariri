from flask_wtf import FlaskForm
from wtforms import SubmitField

class OcorrenciaForm(FlaskForm):
    enviar = SubmitField("Enviar")